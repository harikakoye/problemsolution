from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class ContestsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    contest_id = serializers.IntegerField()
    hacker_id = serializers.IntegerField()
    class Meta:
        model = Contests
        fields = ('id','name','contest_id','hacker_id')

class CollegesSerializer(serializers.ModelSerializer):
    contest_id = ContestsSerializer(many=False)
    college_id = serializers.IntegerField()
    class Meta:
        model = Colleges
        fields = ('id','contest_id','college_id')

#The `.create()` method does not support writable nested fields by default. Write an explicit `.create()` method for serializer `ps.serializers.CollegesSerializer`, or set `read_only=True` on nested serializer fields
#thats why here am using Createserializer
class CollegesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleges
        fields = "__all__"

class ChallengesSerializer(serializers.ModelSerializer):
    college_id = CollegesSerializer(many=False)
    challenge_id = serializers.IntegerField()
    class Meta:
        model = Challenges
        fields = ('id','challenge_id','college_id')
class ChallengesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = "__all__"

class ViewStatsSerializer(serializers.ModelSerializer):
    challenge_id = ChallengesSerializer(many=False)
    total_views = serializers.IntegerField()
    total_unique_views = serializers.IntegerField()
    class Meta:
        model = ViewStats
        fields = ('id','challenge_id','total_views','total_unique_views')
class ViewStatsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStats
        fields = "__all__"


class SubmissionStatsSerializer(serializers.ModelSerializer):
    challenge_id = ViewStatsSerializer(many=False)
    total_accept_submissions = serializers.IntegerField()
    total_submissions = serializers.IntegerField()
    class Meta:
        model = SubmissionStats
        fields = ('challenge_id','total_accept_submissions','total_submissions')
class SubmissionStatsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionStats
        fields = "__all__"
