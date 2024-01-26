# backend/app/models/Interview_model.py
from PyPDF2 import PdfReader


class Interview:
    def __init__(self, job_title, interviewer, candidate, job_description, resume, company): 
        self.job_title = job_title
        self.interviewer = interviewer
        self.candidate = candidate
        self.job_description = job_description
        self.resume = resume
        self.company = company

    def get_job_description_text(self): 
        return open(self.job_description).read()
    
    def get_resume_text(self): 
        return PdfReader(self.resume).pages[0].extract_text()
    
    def get_company_data_text(self): 
        return open(self.company).read()
    





    


