"""
"""
import uuid

from rest_framework import serializers

from dukaan.apps.orders.models import (Cart, ProductInCart, Order, 
	ProductInOrder) 
from dukaan.apps.products.models import Product


class CartSerializer(serializers.Serializer):
	"""
	"""
	cart_id = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(), required=False)
	qty = serializers.IntegerField()
	product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(is_copy=False))

	class Meta:
		fields = ('cart_id', 'product_id', 'qty',)

	def create(self, validated_data):
		"""
		"""
		if validated_data.get('cart_id'):
			cart_obj = validated_data.get('cart_id')
		else:
			cart_obj = Cart.objects.create()
		
		created, obj = ProductInCart.objects.get_or_create(
			product = validated_data['product_id'],
			cart = cart_obj,
			defaults={'quantity': validated_data['qty']}
			)
		if not created and obj.quantity != validated_data['qty']:
			# update new quantity
			obj.quantity = validated_data['qty']
			obj.save()

		return cart_obj


class OrderSerializer(serializers.Serializer):
	"""
	"""
	cart_id = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all())

	class Meta:
		fields = ('cart_id',)

	def create(self, validated_data):
		"""
		"""
		cart = validated_data['cart_id']
		order_obj = Order.objects.create(
			order_by = self.context.get('request').user,
			)
		prod_objs = []
		for cart_product in cart.product_in_cart.all():
			product = cart_product.product
			product.id = None
			product.is_copy = True
			product.save()
			prod_objs.append(ProductInOrder(
				product = product,
				order = order_obj,
				quantity = cart_product.quantity
				))
				
		ProductInOrder.objects.bulk_create(prod_objs)

		# delete cart
		cart.delete()
		return order_obj