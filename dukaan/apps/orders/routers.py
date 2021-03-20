"""
"""
from django.urls import path, include 
from rest_framework.routers import SimpleRouter

# from dukaan.apps.store.views import (
#     TokenAPIView,TokenAssignAPIView
# )


router = SimpleRouter()

# router.register(r'token', TokenViewSet, basename='token')

urlpatterns = [

]

urlpatterns += router.urls
