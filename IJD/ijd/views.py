from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from .models import *
from .serializers import *
from .ai_scripts.ijd_assistant import IJDAssistant
from .ai_scripts.utils import generate_job_description

def home(request):
    #put the actual home page here
    return HttpResponse("Welcome to the Home Page!")

@api_view(['GET'])
@csrf_exempt
def bushel(request): #TODO: add fetching of specific IDs
    response = generate_job_description(
    job_overview_title="How You'll Make An Impact",
    job_overview_list=[
      "Bachelor’s or Master’s degree in Computer Science or related field.",
      "7+ years of proven experience as a Senior Software Engineer with a focus on backend systems.",
      "Experience designing and implementing microservice architecture and associated best practices.",
      "Understanding of event driven design strategies.",
      "In-depth knowledge of message buses (e.g., Apache Pulsar, RabbitMQ) and experience in implementing and managing distributed messaging systems.",
      "Familiarity with API development and scalability.",
      "Expertise in developing and optimizing identity services, including authentication and authorization mechanisms.",
      "Proficient in various programming languages with an emphasis on Java/Kotlin.",
      "Experience with containerization technologies including Kubernetes.",
      "Solid understanding of software development best practices, version control, and CI/CD pipelines.",
      "Experience and knowledge of relational and noSQL database design and implementations.",
      "Ability to implement performant data querying techniques.",
      "Versed in various quality assurance strategies including system, functional, and unit testing.",
      "Strong understanding of security best practices around access and exposure.",
      "Effective problem solving skills, with the ability to analyze complex issues and provide effective solutions.",
      "Excellent communication and collaboration skills.",
    ],
    job_responsibilities_title="",
    job_responsibilities_list=[
      "Design, develop, and maintain scalable and high-performance backend systems utilizing distributed event driven service architecture.",
      "Configure and manage message buses for efficient communication between distributed systems and services.",
      "Expand and optimize existing access management and authentication systems to accommodate custom authorization flows and integrate with third party identity providers.",
      "Evolve existing deployment pipelines to increase time to market capabilities.",
      "Ensure the adoption and evolution of organizational security policies.",
      "Implement appropriate code and system testing strategies.",
      "Track and monitor progress through typical Agile processes.",
      "Conduct code reviews, mentor junior developers, and contribute to a culture of continuous improvement.",
      "Troubleshoot and resolve complex issues in collaboration with operations and support teams.",
      "Collaborate with product partners to provide technical prospective and realistic estimates in establishing team roadmaps.",
      "Provide daily focus on security best practices to ensure data and code protections.",
    ],
    job_requirements_title="What Bushel Is Looking For",
    job_requirements_list=[
      "Bachelor’s or Master’s degree in Computer Science or related field.",
      "7+ years of proven experience as a Senior Software Engineer with a focus on backend systems.",
      "Experience designing and implementing microservice architecture and associated best practices.",
      "Understanding of event driven design strategies.",
      "In-depth knowledge of message buses (e.g., Apache Pulsar, RabbitMQ) and experience in implementing and managing distributed messaging systems.",
      "Familiarity with API development and scalability.",
      "Expertise in developing and optimizing identity services, including authentication and authorization mechanisms.",
      "Proficient in various programming languages with an emphasis on Java/Kotlin.",
      "Experience with containerization technologies including Kubernetes.",
      "Solid understanding of software development best practices, version control, and CI/CD pipelines.",
      "Experience and knowledge of relational and noSQL database design and implementations.",
      "Ability to implement performant data querying techniques.",
      "Versed in various quality assurance strategies including system, functional, and unit testing.",
      "Strong understanding of security best practices around access and exposure.",
      "Effective problem solving skills, with the ability to analyze complex issues and provide effective solutions.",
      "Excellent communication and collaboration skills.",
    ],
    about_the_org_title="Welcome To Bushel's Corner of the Internet",
    about_the_org_list=[
      "Why does Bushel exist? To ensure humanity and our planet have a secure and healthy future. Bushel believes agriculture is the most important industry on the planet. Agriculture’s physical infrastructure could be considered the greatest advancement in the grain industry in the last century. We believe the agriculture industry needs to build a complementary digital infrastructure - that’s where Bushel comes in.",
      "Bushel builds software for the grain industry. Our mission is to connect the Grain Industry through digital infrastructure.",
      "Today, we have the largest network of elevators and growers, connecting the most extensive data set in the industry. How have we done that? By offering real value to growers and grain companies through a digital set of tools.",
      "Bushel is headquartered in Fargo, ND - one of the best places to live if you ask us! This position is remote eligible. See below for the list of eligible states.",
    ],
    compensation_title="Bushel Benefits",
    compensation_list= [
      "$115,000.00 - $140,000.00 Salary/year",
      "Optional Work from Home",
      "Competitive BCBS Health Insurance with contribution to premium",
      "Health Savings Account (HSA) with matching dollars",
      "Flexible Spending Accounts",
      "Dental and Vision Insurance",
      "Hybrid work environment | Flexible working hours | Work-life balance",
      "Basic Life Insurance and Short-Term Disability paid by Bushel",
      "Additional Voluntary Life Insurance options and Long-Term Disability",
      "Voluntary Accident Insurance and Critical Illness Insurance",
      "Flexible (Unlimited) Paid Time Off, 9 Paid Holidays, and 1 Volunteer Day",
      "Up to 12 weeks of Paid Parental Leave, including foster care and adoption",
      "401(k) Retirement with 4% company match with immediate vesting",
      "Employee Assistance Program and BetterHelp counseling services",
      "Learning and development and internal mentorship opportunities",
    ])

    print(response)

    return JsonResponse(response, safe=False)




@api_view(['POST'])
@csrf_exempt
def generate_ijd_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data['question']
            
            # Initialize the IJDAssistant and ask the question
            ijd_assistant = IJDAssistant()
            response = ijd_assistant.ask_question(question)
            
            # Send back the response in JSON format
            return JsonResponse({'response': response}, status=200)
        except KeyError:
            return JsonResponse({'error': 'Missing question in request'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = IJDUser.objects.all()
    serializer_class = IJDUserSerializer

class ApplicantProfileViewSet(viewsets.ModelViewSet):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobDetailViewSet(viewsets.ModelViewSet):
    queryset = JobDetail.objects.all()
    serializer_class = JobDetailSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class UserQuestionViewSet(viewsets.ModelViewSet):
    queryset = UserQuestion.objects.all()
    serializer_class = UserQuestionSerializer

class AIResponseViewSet(viewsets.ModelViewSet):
    queryset = AIResponse.objects.all()
    serializer_class = AIResponseSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer