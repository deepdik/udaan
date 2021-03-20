"""
"""
from django.urls import path, include 
from rest_framework.routers import SimpleRouter

from dukaan.apps.udaan_app.views import (QuizViewSet,
	QuestionViewSet)


router = SimpleRouter()

router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'question', QuestionViewSet, basename='question')

urlpatterns = [

]

urlpatterns += router.urls

