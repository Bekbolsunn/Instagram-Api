from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     GenericAPIView, )
from rest_framework import status
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        AllowAny)
from .serializers import (RegisterSerializers,
                          LoginSerializer,)
from .models import CustomUser


class RegisterUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializers
    # permission_classes = (AllowAny,)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    # permission_classes = (AllowAny,)

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
