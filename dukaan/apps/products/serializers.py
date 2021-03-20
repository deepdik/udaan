"""
"""
import uuid

from rest_framework import serializers

from dukaan.apps.products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
	"""
	"""
	category = serializers.CharField(source='category.name')

	class Meta:
		model = Product
		fields = ('id', 'name', 'description', 'mrp',
			'sale_price', 'image', 'category')

		extra_kwargs = {
			'description': {'write_only': True},
			'mrp': {'write_only': True},
			'sale_price': {'write_only': True},
			'category': {'write_only': True},
		}

	def create(self, validated_data):
		"""
		"""
		validated_data['created_by'] = self.context.get('request').user
		cat_obj, created= Category.objects.get_or_create(
			name__icontains=validated_data['category']['name'],
			defaults={'name': validated_data['category']['name']}
		)
		validated_data['store'] = self.context.get('store_obj')
		validated_data['category'] = cat_obj
		obj = super().create(validated_data)
		return obj


class ProductsDetailSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = Product
		fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
	"""
	"""
	products = serializers.SerializerMethodField()

	def get_products(self, obj):
		"""
		"""
		qs = obj.product.filter(is_copy = False)
		return ProductsDetailSerializer(qs, many=True).data

	class Meta:
		model = Category
		fields = ('id', 'name', 'products')
