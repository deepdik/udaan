import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
	"""
	"""
	product = models.ManyToManyField('products.Product', 
		through="orders.ProductInOrder", related_name='order')
	order_by = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE, related_name='order')
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)


class ProductInOrder(models.Model):
	"""
	"""
	product = models.ForeignKey('products.Product', 
		on_delete=models.CASCADE, related_name='product_in_order')
	order = models.ForeignKey('orders.Order',
		on_delete=models.CASCADE, related_name='product_in_order')
	quantity = models.PositiveIntegerField()


class Cart(models.Model):
	"""
	"""
	products = models.ManyToManyField('products.Product', 
		related_name='cart', through="orders.ProductInCart")
	added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE, related_name='cart', blank=True, 
		null=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)


class ProductInCart(models.Model):
	"""
	"""
	product = models.ForeignKey('products.Product', 
		on_delete=models.CASCADE, related_name='product_in_cart')
	cart = models.ForeignKey('orders.Cart',
		on_delete=models.CASCADE, related_name='product_in_cart')
	quantity = models.PositiveIntegerField()
