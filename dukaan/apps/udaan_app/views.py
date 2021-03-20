"""
"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from dukaan.apps.udaan_app.models import (Question, QuestionOptions, 
	Quiz, QuizResponse, UserQuestionReponse)

from dukaan.apps.udaan_app.serializers import (
	QuizSerializer, QuestionSerializer, QuestionOptionsSerializer,
	QuizResponseSaveSerializer)


class QuizViewSet(viewsets.ModelViewSet):
	"""
	"""
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer


	@action(detail=True, methods=['post'], url_path='save-quiz-response')
	def save_quiz_response(self, request, *args, **kwags):
		"""
		"""
		obj = self.get_object()
		serializer = QuizResponseSaveSerializer(data=request.data,
		 	many=True, context={'obj':obj})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response('save successfully', 200)


class QuestionViewSet(viewsets.ModelViewSet):
	"""
	"""
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer


	@action(detail=True, methods=['post'], url_path='save-options')
	def save_question_options(self, request, *args, **kwags):
		"""
		"""
		obj = self.get_object()
		serializer = QuestionOptionsSerializer(data=request.data,
		 	many=True, context={'quest':obj})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response('save successfully', 200)
