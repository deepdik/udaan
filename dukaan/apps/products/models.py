import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
	"""
	To store categories
	"""
	name = models.CharField(max_length=100)

	class Meta:
		db_table = 'category'
		permissions = ()


class Product(models.Model):
	"""
	To store products
	"""
	category = models.ForeignKey('products.Category', 
		on_delete=models.CASCADE, related_name='product')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE, related_name='product')
	store = models.ForeignKey('store.Store', 
		on_delete=models.CASCADE, related_name='product')
	name = models.CharField(_('product name'), max_length=100)
	description = models.TextField(_('description'),
		max_length=300)
	mrp = models.PositiveIntegerField(_('MRP'))
	sale_price = models.PositiveIntegerField(_('sale price'))

	image = models.ImageField(upload_to="productImg", blank=True, null=True)
	is_copy = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		db_table = 'product'
		permissions = ()
