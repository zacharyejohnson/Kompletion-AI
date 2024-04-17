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

def home(request):
    #put the actual home page here
    return HttpResponse("Welcome to the Home Page!")

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