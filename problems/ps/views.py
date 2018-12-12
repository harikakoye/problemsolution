from django.shortcuts import render
from rest_framework.status import HTTP_202_ACCEPTED
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework import routers, serializers, viewsets
import re
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class ContestsViewSet(viewsets.ModelViewSet):
    queryset = Contests.objects.all()
    serializer_class = ContestsSerializer

class CollegesViewSet(viewsets.ModelViewSet):
    queryset = Colleges.objects.all()
    serializer_class = CollegesCreateSerializer

class ChallengesViewSet(viewsets.ModelViewSet):
    queryset = Challenges.objects.all()
    serializer_class = ChallengesCreateSerializer

class ViewStatsViewSet(viewsets.ModelViewSet):
    queryset = ViewStats.objects.all()
    serializer_class = ViewStatsCreateSerializer

class SubmissionStatsViewSet(viewsets.ModelViewSet):
    queryset = SubmissionStats.objects.all()
    serializer_class = SubmissionStatsCreateSerializer

