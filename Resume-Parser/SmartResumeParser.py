from PyPDF2 import PdfReader
import openai
import json

class SmartResumeParser: 
    def __init__(self, resume_path, API_KEY): 

        self.API_KEY = API_KEY
        # base attributes that will be pulled automatically from any resume 
        self.base_attribute_names = ["fname", "lname", "email_address", "phone_number", "experience", "education"]

        self.openai_connection_established = False

        
      
        # connect to OpenAI via api key 
        self.openai_client = openai.OpenAI(api_key=API_KEY)
        resume_text = self.parse_resume_text(resume_path)

        # create assistant object via OpenAI's API 
        self.parsing_assistant = self.openai_client.beta.assistants.create(
                name="Resume JSON Parser", 
                instructions=f"You are a resume parser. You will be given the text from a resume,\
                        and a set of attributes to parse from the resume. \
                        Your response should be only the attributes you have parsed from the resume in a \
                        JSON format as so: {{attribute_name: parsed_attribute_value}} for each \
                        attribute in the list of attributes. Your output MUST be able to be immediately\
                        converted to a python dictionary. Here is the resume from which you will be asked to parse attributes from:\
                            {resume_text}. Please prepare to recieve input in the form of a list of attributes to be parsed.", 
                model="gpt-3.5-turbo-1106",   
        )
        self.thread = self.openai_client.beta.threads.create()

        self.openai_connection_established = True
            

    # main function for parsing attributes from resume 
    def parse_attributes_from_resume(self, attributes): 
            attributes_list = "[" + ', '.join(attributes) + "]"
            message = self.openai_client.beta.threads.messages.create(
                thread_id=self.thread.id, 
                role="user", 
                content=f"attributes to parse: {attributes_list}"
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

                    print(return_string)

                    response = json.loads(return_string)

                    return response
 


    def parse_resume_text(self, resume_path):

            # Ensure the PDF file is readable
            resume_text = ""

            try:
                # Open the PDF file
                reader = PdfReader(resume_path)
                # Extract text from the first page
                resume_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            except Exception as e:
                return {"error": f"Failed to read PDF: {str(e)}"}
            return resume_text
        
    
            

        
if __name__ == '__main__': 

    parser = SmartResumeParser("C:\\Users\\NDSU-Prof\\Documents\\GitHub\\Resume-Parser\\Zach Johnson Resume 2024.pdf", API_KEY="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")         

    print(parser.parse_attributes_from_resume(["fname", "lname", "email", "phone_number", "experience"]))

    print("\n\ntrying to parse custom attributes\n\n")

    print(parser.parse_attributes_from_resume(["HAS_EXPERIENCE_WITH_JAVA", "HAS_EXPERIENCE_WITH_REACT", "RATING_1_TO_100"]))


        
