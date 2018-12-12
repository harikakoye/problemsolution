from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
#from django.contrib import admin
# Create your models here.

class Contests(models.Model):
    name = models.CharField(max_length=255)
    contest_id= models.IntegerField()
    hacker_id = models.IntegerField()
    def __str__(self):
        return self.name + "_" + str(self.contest_id) + str(self.hacker_id)

class Colleges(models.Model):
    contest_id = models.ForeignKey(Contests)
    college_id = models.IntegerField()
    def __str__(self):
        return str(self.college_id) + " - " + str(self.contest_id)

class Challenges(models.Model):
    challenge_id = models.IntegerField()
    college_id = models.ForeignKey(Colleges)
    def __str__(self):
        return str(self.challenge_id) + " - " + str(self.college_id)

class ViewStats(models.Model):
    challenge_id = models.ForeignKey(Challenges)
    total_views = models.IntegerField()
    total_unique_views = models.IntegerField()
    def __str__(self):
        return str(self.challenge_id) + " - " + str(self.total_views) + "_" + str(self.total_unique_views)

class SubmissionStats(models.Model):
    challenge_id = models.ForeignKey(Challenges)
    total_accept_submissions = models.IntegerField()
    total_submissions = models.IntegerField()

    def __str__(self):
        return str(self.challenge_id) + " - " + str(self.total_submissions) + "_" + str(self.total_accept_submissions)


#admin.site.register(Contests)
#admin.site.register(Colleges)
#admin.site.register(Challenges)
#admin.site.register(ViewStats)
#admin.site.register(SubmissionStats)
