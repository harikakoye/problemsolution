from django.conf.urls import url,include

from ps.views import ContestsViewSet, CollegesViewSet, ChallengesViewSet, ViewStatsViewSet, SubmissionStatsViewSet
from .import views
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'Contests',views.ContestsViewSet,'Contests')
router.register(r'Colleges',views.CollegesViewSet,'Colleges')
router.register(r'Challenges',views.CollegesViewSet,'Challenges')
router.register(r'ViewStats',views.CollegesViewSet,'ViewStats')
router.register(r'SubmissionStats',views.CollegesViewSet,'SubmissionStats')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^Contests/', ContestsViewSet),
    url(r'^Colleges/', CollegesViewSet),
    url(r'^Challenges/', ChallengesViewSet),
    url(r'^ViewStats/', ViewStatsViewSet),
    url(r'^SubmissionStats/', SubmissionStatsViewSet),

]

