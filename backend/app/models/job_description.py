# backend/app/models/Job_description_model.py
from app import db

class JobDescription(db.Model):
    __tablename__ = 'job_descriptions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    responsibilities = db.Column(db.Text, nullable=False)
    qualifications = db.Column(db.Text)
    # More fields as needed

    # Relationships
    # For example, if there's a relationship between job descriptions and interviews
    interviews = db.relationship('Interview', backref='job_description', lazy=True)

    def __repr__(self):
        return f'<JobDescription {self.title}>'
