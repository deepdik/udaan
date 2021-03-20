"""
"""
from django.urls import path, include 
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

#router.register(r'product', ProductViewset, basename='product')

urlpatterns = [

]

urlpatterns += router.urls
