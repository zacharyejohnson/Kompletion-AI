import hashlib
from PyPDF2 import PdfReader
import openai
import json
import sqlite3
import resume_database
from resume_database import Resume, Experience, Education
import logging

class SmartResumeParser: 
    def __init__(self, API_KEY): 

        self.db_session = resume_database.activate_db_session()
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



        self.API_KEY = API_KEY
        # base attributes that will be pulled automatically from any resume 
        self.base_attribute_names = ["fname", "lname", "email_address", "phone_number", "experience", "education"]

        self.openai_connection_established = False

        
      
        # connect to OpenAI via api key 
        self.openai_client = openai.OpenAI(api_key=API_KEY)

        # create assistant object via OpenAI's API 
        self.parsing_assistant = self.openai_client.beta.assistants.retrieve("asst_RzJ8pC5mkeSl47CUICbzxdj8")
        # (
        #         name="Resume JSON Parser", 
        #         instructions="You are a resume parser. You will be given the text from a resume,\
        #                 and a set of attributes to parse from the resume. \
        #                 Your response should be only the attributes you have parsed from the resume in a \
        #                 JSON format as so: {attribute_name: parsed_attribute_value} for each \
        #                 attribute in the list of attributes. education should be in a nested json format with subfields specific to education (null if you cant find it, end_date current if they are not done): [degree, field_of_study, institution, gpa, location, start_date, end_date]\
        #                       for each education listed. \experience should follow a similar nested format with fields(end_date = current if current): [job_title, company, start_date, end_date, details]. \
        #                           Your output MUST be able to be immediately converted to a json object. Dates should be in the form yyyy-mm-dd.\
        #                           an example output would be {\"fname\": *parsed_fname*, \"lname\": *parsed_lname*, \"email\": *parsed_email*, ..., \"education\": [{\"attr\": parsed_attr_val for val in list_given_earleir}], ... and so on }\
        #                     Please prepare to recieve input in the form of raw resume text, and a list of attributes to be parsed.", 
        #         model="gpt-3.5-turbo-1106",   
        # )
        self.thread = self.openai_client.beta.threads.create()

        self.openai_connection_established = True
            

    # main function for parsing attributes from resume 
    def parse_attributes_from_resume(self, resume_path, attributes): 
            try: 
                resume_text = self.parse_resume_text(resume_path)
            except Exception as e: 
                return f"Error reading resume: {e}"

            attributes_list = "[" + ', '.join(attributes) + "]"
            existing_resume = self.existing_resume(resume_text)

            if existing_resume == None: 
                message = self.openai_client.beta.threads.messages.create(
                    thread_id=self.thread.id, 
                    role="user", 
                    content=f"attributes to parse:\n{attributes_list},\n\nresume:\n{resume_text}"
                )
                run = self.openai_client.beta.threads.runs.create(
                    thread_id=self.thread.id, 
                    assistant_id=self.parsing_assistant.id, 
                    
                )

                while run.status in ["queued", "in_progress"]:
                    keep_retrieving_run = self.openai_client.beta.threads.runs.retrieve(
                        thread_id=self.thread.id,
                        run_id=run.id
                    )
                    print(f"Run status: {keep_retrieving_run.status}")
                    if keep_retrieving_run.status == "completed": 

                        responses = self.openai_client.beta.threads.messages.list(thread_id=self.thread.id)
                        return_string = responses.data[0].content[0].text.value

                        #print(return_string)

                        parsed_attrs = json.loads(return_string)                     
                             
                        self.add_resume(self.db_session, parsed_attrs, resume_text)

                        return parsed_attrs
            else: 
                 parsed_attrs = []
                 for attr in attributes: 
                      parsed_attrs.append(getattr(existing_resume, attr))                      
 
    
    def existing_resume(self, resume_text):
        """
        Checks if a resume with the given text already exists in the database.
        """
        resume_text_hash = hashlib.sha256(resume_text.encode('utf-8')).hexdigest()
        existing_resume = self.db_session.query(Resume).filter_by(resume_text_hash=resume_text_hash).first()
        return existing_resume

    def parse_resume_text(self, resume_path):
        resume_text = ""
        try:
            reader = PdfReader(resume_path)
            resume_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            logging.info(f"Successfully parsed resume text from {resume_path}")
        except Exception as e:
            logging.error(f"Failed to read PDF {resume_path}: {str(e)}")
            resume_text = {"error": f"Failed to read PDF: {str(e)}"}
        return resume_text

        
    def add_resume(self, session, parsed_attrs, resume_text):
            try: 
                # Calculate the hash of the resume text
                resume_hash = hashlib.sha256(resume_text.encode('utf-8')).hexdigest()

                
                # add it to the database
                new_resume = Resume(fname=parsed_attrs["fname"],
                                    lname=parsed_attrs["lname"],
                                    email_address=parsed_attrs["email_address"],
                                    phone_number=parsed_attrs["phone_number"],
                                    resume_text_hash=resume_hash)
                
                session.add(new_resume)

                print(parsed_attrs["educations"])
                # multiple educations listed; add each to DB
                for parsed_education in parsed_attrs["educations"]: 
                    
                    new_education = Education(institution_name = parsed_education["institution"],
                                            degree=parsed_education["degree"], 
                                            field_of_study=parsed_education["field_of_study"], 
                                            start_date = parsed_education["start_date"], 
                                            end_date = parsed_education["end_date"], 
                                            resume_id = new_resume.id)
                    session.add(new_education)

                for parsed_experience in parsed_attrs["experiences"]: 
                    print(parsed_experience)


                    new_experience = Experience(company_name = parsed_experience["company"], 
                                                job_title = parsed_experience["job_title"], 
                                                start_date = parsed_experience["start_date"], 
                                                end_date = parsed_experience["end_date"], 
                                                description = parsed_experience["details"], 
                                                resume_id = new_resume.id)
                    
                    session.add(new_experience)
            
                    logging.info("New resume added to the database.")
            except Exception as e:
                session.rollback()
                logging.error(f"Failed to add new resume to the database: {str(e)}")
                    
                session.commit()
            return new_resume.id
    

if __name__ == '__main__': 

    # little demo

    parser = SmartResumeParser(API_KEY="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")   

    resumes = ["data\Zach Johnson Resume 2024.pdf", "data\construction-resume-example.pdf"] 

    for resume_path in resumes: 
         
        print(parser.parse_attributes_from_resume(resume_path, ["fname", "lname", "email_address", "phone_number", "educations", "experiences"]))

    #print(parser.parse_attributes_from_resume(["HAS_EXPERIENCE_WITH_JAVA", "HAS_EXPERIENCE_WITH_REACT", "RATING_1_TO_100"]))

    # To fetch and display all resumes from the database
    all_resumes = parser.db_session.query(resume_database.Resume).all()

    print("\nAll Resumes in Database:\n")
    for resume in all_resumes:
        print(f"ID: {resume.id}, First Name: {resume.fname}, Last Name: {resume.lname}, Email: {resume.email_address}, Phone: {resume.phone_number}")
        # Optionally print experiences and educations if needed
        for exp in resume.experiences:
            print(f"  Experience - Company: {exp.company_name}, Title: {exp.title}, Start: {exp.start_date}, End: {exp.end_date}, Description: {exp.description}")
        for edu in resume.educations:
            print(f"  Education - Institution: {edu.institution_name}, Degree: {edu.degree}, Field: {edu.field_of_study}, Start: {edu.start_date}, End: {edu.end_date}")
        print("\n") 