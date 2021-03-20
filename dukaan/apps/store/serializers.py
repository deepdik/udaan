"""
"""
import uuid

from django.conf import settings

from rest_framework import serializers
from rest_framework.reverse import reverse

from dukaan.apps.store.models import Store


class StoreSerializer(serializers.ModelSerializer):
	"""
	"""
	store_link = serializers.CharField(allow_blank=True, required=False)

	class Meta:
		model = Store
		lookup_field = 'slug'
		fields = ('id', 'store_name', 'address', 'store_link')
		extra_kwargs = {
			'store_name': {'write_only': True},
			'address': {'write_only': True},
		}

	def create(self, validated_data):
		"""
		"""
		validated_data['created_by'] = self.context.get('request').user
		obj = super().create(validated_data)
		obj.store_link = settings.SITE_URL+ '/api/v1/store/' +obj.slug
		return obj


class StoreDetailSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = Store
		fields = ('id', 'store_name', 'address')
