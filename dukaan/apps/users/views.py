import datetime

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from dukaan.apps.users.serializers import UserCreateSerializer
from dukaan.libs.accounts.models import Account


class SellerSignup(APIView):
    """
    *To get authorization token from user credentials*.
    """
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
        	data=request.data,
        	context = {'request':request, 'user_type': Account.SELLER})
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response({'token':obj.token}, status=status.HTTP_201_CREATED)


class CustomerSignup(APIView):
    """
    *To get authorization token from user credentials*.
    """
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
        	data=request.data,
        	context = {'request':request, 'user_type': Account.CUSTOMER})
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response({'token':obj.token}, status=status.HTTP_201_CREATED)
