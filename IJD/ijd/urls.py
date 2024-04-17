from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register your viewsets with it.
router = DefaultRouter()

# Registering each viewset with the router
router.register(r'users', UserViewSet, basename='users')
router.register(r'applicant_profiles', ApplicantProfileViewSet, basename='applicant_profiles')
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'job_postings', JobPostingViewSet, basename='job_postings')
router.register(r'job_details', JobDetailViewSet, basename='job_details')
router.register(r'faqs', FAQViewSet, basename='faqs')
router.register(r'user_questions', UserQuestionViewSet, basename='user_questions')
router.register(r'ai_responses', AIResponseViewSet, basename='ai_responses')
router.register(r'images', ImageViewSet, basename='images')
router.register(r'resumes', ResumeViewSet, basename='resumes')
#router.register(r"bushel", bushel, basename="bushel")

# Include the router URL patterns
urlpatterns = [
    path("ijd/bushel", bushel, name="bushel"),
    path('', home,  name='home'),
    #path('ijd/', name='home'),
    path('ijd/generate_ijd_response/', generate_ijd_response, name='generate_ijd_response'),
    path('ijd/', include(router.urls)),  # Including all registered viewsets

]
