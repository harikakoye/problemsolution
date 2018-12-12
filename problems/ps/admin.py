from django.contrib import admin
from ps.models import Colleges, Contests, Challenges, ViewStats, SubmissionStats


class CollegesAdmin(admin.ModelAdmin):
    list_display = ('college_id','id')
    list_per_page = 25

class ContestsAdmin(admin.ModelAdmin):
    list_display = ('name','contest_id','hacker_id')
    list_per_page = 25

class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('challenge_id', 'id')
    list_per_page = 25

class ViewStatsAdmin(admin.ModelAdmin):
    list_display = ('challenge_id', 'total_views','total_unique_views')
    list_per_page = 25

class SubmissionStatsAdmin(admin.ModelAdmin):
    list_display = ('challenge_id', 'total_submissions','total_accept_submissions')
    list_per_page = 25

admin.site.register(Colleges, CollegesAdmin)
admin.site.register(Contests, ContestsAdmin)
admin.site.register(Challenges, ChallengesAdmin)
admin.site.register(ViewStats, ViewStatsAdmin)
admin.site.register(SubmissionStats, SubmissionStatsAdmin)