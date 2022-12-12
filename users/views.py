from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (ListCreateAPIView,
                                     ListAPIView)
from rest_framework import status, response
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        AllowAny)

from .serializers import RegisterSerializers
from .models import CustomUser


class RegisterUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = (AllowAny,)

