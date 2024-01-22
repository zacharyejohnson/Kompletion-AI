# backend/app/models/Interview_model.py
from app import db

class Interview:
    def __init__(self, interviewer, candidate, job_description, resume, company): 
        self.interviewer = interviewer
        self.candidate = candidate
        self.job_description = job_description
        self.resume = resume
        self.company = company


        

    


