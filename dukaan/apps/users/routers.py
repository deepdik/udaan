"""
"""
from django.urls import path, include 
from rest_framework.routers import SimpleRouter

from dukaan.apps.users.views import (
    SellerSignup,
    CustomerSignup
)


router = SimpleRouter()

# router.register(r'token', TokenViewSet, basename='token')

urlpatterns = [

	path('seller/signup/', SellerSignup.as_view(), name='seller-signup'),
	path('customer/login/', CustomerSignup.as_view(), name='customer-login'),

]

urlpatterns += router.urls
