from django.db import models
from django.contrib.auth.models import AbstractUser

# User model with custom fields
class IJDUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="ijd_user_set",  # unique related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="ijd_user_set",  # unique related_name
        related_query_name="user_permission",
    )    

# Applicant profile linked to the User
class ApplicantProfile(models.Model):
    user = models.ForeignKey(IJDUser, on_delete=models.CASCADE)
    resume_link = models.TextField(blank=True, null=True)
    portfolio_link = models.TextField(blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    application_history = models.TextField(blank=True, null=True)

# Company model
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    logo_url = models.TextField(blank=True, null=True)

# Job Posting model
class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

# Extended Job Details model
class JobDetail(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # e.g., benefits, company_culture
    content = models.TextField()

# FAQs linked to Job Postings
class FAQ(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

# User questions logged for LLM processing
class UserQuestion(models.Model):
    user = models.ForeignKey(IJDUser, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    question_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# AI Responses to User Questions
class AIResponse(models.Model):
    question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE)
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Image model for multimedia content associated with job postings
class Image(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    image_url = models.TextField()
    description = models.TextField(blank=True, null=True)

# Resume model for storing user resumes
class Resume(models.Model):
    user = models.ForeignKey(IJDUser, on_delete=models.CASCADE)
    file_url = models.TextField()
    file_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=50)
    version = models.IntegerField(default=1)