from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.response import Response
# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        ser = RegisterSerializer(data=request.data) #recieve the data and validate using serializer 
        ser.is_valid(raise_exception=True)
        user = ser.save() #saving on the db
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        ser = LoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        
        user = ser.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {'id': user.id, 'username': user.username, 'email':user.email}
        })
        
class CookieTokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token") #getting the refreshed token from httpOnly cookies
        if not refresh_token:
            return Response({"Detail":"No refresh token"},status=400)
        
        try:
            refresh = RefreshToken(refresh_token)
            acess_token = str(refresh.access_token)
            return Response({"access":acess_token})
        except Exception:
            raise InvalidToken("Invalid refresh token")
        
class MeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        u = request.user
        return Response({
            'id': u.id,
            'username': u.username,
            'email':u.email
        })
        
class LogoutView(APIView):
    def post(self, request):
        response = Response({"detail": "Logged out"})
        response.delete_cookie
        return response