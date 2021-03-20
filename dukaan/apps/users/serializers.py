"""
"""
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
	"""
	"""
	otp = serializers.IntegerField()
	number = serializers.IntegerField()

	class Meta:
		fields = ('number', 'otp')

	def create(self, validated_data):
		"""
		"""
		obj, created = User.objects.get_or_create(
			mobile_no=validated_data['number'],
			defaults={'user_type': self.context.get('user_type')}
			)
		token, created = Token.objects.get_or_create(user=obj)
		obj.token = token.key
		return obj
