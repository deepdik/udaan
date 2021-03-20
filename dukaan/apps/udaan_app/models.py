import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
	"""
	"""
	question = models.TextField()


class QuestionOptions(models.Model):
	"""
	"""
	question = models.ForeignKey('udaan_app.Question',
		on_delete=models.CASCADE, related_name='options')
	option = models.TextField()
	is_ans = models.BooleanField(default=False)


class Quiz(models.Model):
	"""
	"""
	questions = models.ManyToManyField('udaan_app.Question',
		related_name='quiz')


class QuizResponse(models.Model):
	"""
	"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='quiz_response')
	quiz_id = models.ForeignKey('udaan_app.Quiz', on_delete=models.CASCADE,
		related_name='quiz_response')
	
	question_ans = models.ManyToManyField('udaan_app.Question',
		through="udaan_app.UserQuestionReponse", related_name='quiz_response')


class UserQuestionReponse(models.Model):
	"""
	"""
	quiz_qesponse= models.ForeignKey('udaan_app.QuizResponse',
		on_delete=models.CASCADE, related_name='user_resp')
	question = models.ForeignKey('udaan_app.Question',
		on_delete=models.CASCADE, related_name='user_resp')
	user_ans = models.ForeignKey('udaan_app.QuestionOptions',
		on_delete=models.CASCADE, related_name='user_resp')
