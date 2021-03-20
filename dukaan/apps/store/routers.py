"""
"""
from django.urls import path, include 
from rest_framework.routers import SimpleRouter

from dukaan.apps.store.views import (
    StoreViewset
)


router = SimpleRouter()

router.register(r'store', StoreViewset, basename='store')

urlpatterns = [

]

urlpatterns += router.urls
