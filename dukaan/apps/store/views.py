"""
"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from dukaan.apps.orders.models import Cart, Order
from dukaan.apps.orders.serializers import CartSerializer, OrderSerializer
from dukaan.apps.products.models import Category
from dukaan.apps.products.serializers import (ProductSerializer,
	ProductListSerializer)
from dukaan.apps.store.serializers import (StoreSerializer,
	StoreDetailSerializer)
from dukaan.apps.store.models import Store


class StoreViewset(viewsets.ModelViewSet):
	"""
	"""
	queryset = Store.objects.all()
	lookup_field = 'slug'
	permission_classes_by_action = {
		'create': (permissions.IsAuthenticated,),
		'retrieve': (permissions.AllowAny,)
	}

	def get_permissions(self):
		"""
		"""
		try:
			# return permission_classes depending on `action` 
			return [permission() for permission
				 in self.permission_classes_by_action[self.action]]
		except KeyError: 
			# action is not set return default permission_classes
			return [permission() for permission in self.permission_classes]

	def get_serializer_class(self):
		"""
		"""
		if self.action == 'retrieve':
			return StoreDetailSerializer
		return StoreSerializer

	@action(detail=True, methods=['post'], url_path='product-create')
	def get_product_create(self, request, *args, **kwags):
		"""
		"""
		store_obj = self.get_object()
		serializer = ProductSerializer(data=request.data,
			 context={'request': request, 'store_obj':store_obj})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	@action(detail=True, methods=['get'], url_path='product-lists')
	def get_product_list(self, request, *args, **kwags):
		"""
		"""
		obj = self.get_object()
		cats = Category.objects.filter(
			product__store=obj,
			product__is_copy=False
			).distinct()
		data = ProductListSerializer(cats, many=True).data
		return Response(data, 200)

	@action(detail=True, methods=['post'], url_path='add-in-cart')
	def add_in_cart(self, request, *args, **kwags):
		"""
		"""
		# add in cart
		serializer = CartSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		obj = serializer.save()
		return Response(
			{
			'msg': 'Product added in cart.Please pass cart'+
			 	'id to add product in same cart',
			'cart_id': obj.id
			},
			status=status.HTTP_201_CREATED
		)

	@action(detail=True, methods=['post'], url_path='place-order')
	def place_order(self, request, *args, **kwags):
		"""
		"""
		if request.user.is_authenticated:
			serializer = OrderSerializer(
				data=request.data,
				context = {'request': request}
			)
			serializer.is_valid(raise_exception=True)
			obj = serializer.save()
			return Response(
				{
				'msg': 'Order placed successfully',
				'order_id': obj.id
				},
				status=status.HTTP_201_CREATED
			)

		return Response(
				{
				'msg': 'Please Login to place a order',
				},
				status=200
			)
