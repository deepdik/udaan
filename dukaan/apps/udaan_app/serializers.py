"""
"""
import uuid

from rest_framework import serializers

from dukaan.apps.udaan_app.models import *


class QuizSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = Quiz
		fields = ('questions',)


class QuestionSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = Question
		fields = ('id', 'question',)


class QuestionOptionsSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = QuestionOptions
		fields = ('option', 'is_ans',)

	def create(self, validated_data):
		"""
		"""
		objs = []
		for data in validated_data:
			objs.append(QuestionOptions(
				question = self.context.get('quest'),
				option = validated_data['option'],
				is_ans = validated_data['is_ans']
				))

		QuestionOptions.objects.bulk_create(objs)


class ResponseSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = UserQuestionReponse
		fields = ('question', 'user_ans',)


class QuizResponseSaveSerializer(serializers.ModelSerializer):
	"""
	"""
	question_ans = ResponseSerializer(many=True)

	class Meta:
		model = QuizResponse
		fields = ('user', 'quiz_id', 'question_ans')

	def create(self, validated_data):
		"""
		"""
		quiz_obj = QuizResponse.objects.create(
			user =  validated_data['user'],
			quiz_id = self.context.get('obj')
			)
		objs = []
		for data in validated_data['question_ans']:
			objs.append(UserQuestionReponse(
				quiz_qesponse = quiz_obj,
				question = validated_data['question'],
				user_ans = validated_data['user_ans']
				))

		QuestionOptions.objects.bulk_create(objs)

		return quiz_obj
