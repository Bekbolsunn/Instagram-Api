# django imports
from django.contrib.auth import login, authenticate
from rest_framework import views, generics, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# local imports
from .models import CustomUser
from .services import GetLoginResponseService
from .serializers import RegisterSerializers, LoginSerializer, ProfileSerializer
from .pagination import ProfilePagination






class RegisterUserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]


class LoginAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            raise AuthenticationFailed()
        login(request, user)
        return Response(data=GetLoginResponseService.get_login_response(user, request))


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
    authentication_classes = [
        JWTAuthentication,
    ]
    pagination_class = ProfilePagination
    # filter_backends = [
    #     DjangoFilterBackend,
    # ]
    # filterset_class = UserFilter
