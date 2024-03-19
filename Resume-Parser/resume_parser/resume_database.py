from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from contextlib import contextmanager

# Global variable for the base model
Base = declarative_base()

def activate_db_session(db_path='sqlite:///resume_data.db'):
    """
    Initializes the database by creating an engine and a session factory.
    This function should be called before using any functionality that requires database access.

    :param db_path: The database path, defaults to 'sqlite:///resume_data.db'

    :returns session: the database session to be used
    """
    # Create an engine that stores data in the specified SQLite database file
    engine = create_engine(db_path, echo=True, future=True)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    # Create a sessionmaker bound to the engine
    Session = sessionmaker(bind=engine)

    return Session()


#  Resume class which will be mapped to the "resumes" table
# Each attribute represents a column in the table
class Resume(Base):
    __tablename__ = 'resumes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    phone_number = Column(String)
    resume_text_hash = Column(String, unique=True)  # Ensure hash uniqueness in the table
    
    # Establish relationships to Experience and Education tables
    experiences = relationship("Experience", backref="resume")
    educations = relationship("Education", backref="resume")

class Experience(Base):
    __tablename__ = 'experiences'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    start_date = Column(String)
    end_date = Column(String)
    description = Column(Text)
    resume_id = Column(Integer, ForeignKey('resumes.id'))

class Education(Base):
    __tablename__ = 'educations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    institution_name = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field_of_study = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    resume_id = Column(Integer, ForeignKey('resumes.id'))

def add_resume(session, fname, lname, email_address, phone_number, resume_text_hash):
    new_resume = Resume(fname=fname, lname=lname, email_address=email_address, phone_number=phone_number, resume_text_hash=resume_text_hash)
    session.add(new_resume)
    session.commit()
    return new_resume.id

def add_experience(session, resume_id, company_name, job_title, start_date=None, end_date=None, description=None):
    new_experience = Experience(resume_id=resume_id, company_name=company_name, job_title=job_title, start_date=start_date, end_date=end_date, description=description)
    session.add(new_experience)
    session.commit()

def add_education(session, resume_id, institution_name, degree, field_of_study=None, start_date=None, end_date=None):
    new_education = Education(resume_id=resume_id, institution_name=institution_name, degree=degree, field_of_study=field_of_study, start_date=start_date, end_date=end_date)
    session.add(new_education)
    session.commit()

