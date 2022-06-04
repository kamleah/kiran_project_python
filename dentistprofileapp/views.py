from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
# ---- Import all models here
from dentistprofileapp.models import Registration

# ---- Import all serializers here
from dentistprofileapp.serializers import RegistrationSerializer, ViewRegistrationSerializer
# Create your views here.


class Registrations(APIView):

    def get(self, request):
        requestRegistration = Registration.objects.all().order_by('-id')
        requestRegistrationSerializer = ViewRegistrationSerializer(
            requestRegistration, many=True)
        return Response(requestRegistrationSerializer.data)

    def post(self, request, format=None):
        try:
            Registration.objects.get(name__iexact=request.data['name'])
            return Response({"Message": "Email is already exists"})
        except Registration.DoesNotExist:
            RegistrationData = RegistrationSerializer(data=request.data)
            if RegistrationData.is_valid():
                RegistrationData.save()
                return Response({'Message': 'Registration Sucessfull Done'})
            return Response(RegistrationData.errors)


class Login(APIView):

    def post(self, request):
        name = request.data['name']
        password = request.data['password']
        try:
            checkname = Registration.objects.get(name__iexact=name)
            if checkname:
                checkpassword = check_password(password, checkname.password)
                if checkpassword:
                    refresh = RefreshToken.for_user(checkname)
                    return Response({"Message": "Login Sucessfull", 'refresh': str(refresh),'access': str(refresh.access_token)})
                return Response({'Message': 'Please provide valid credentials'})
        except Registration.DoesNotExist:
            return Response({'Message': 'Please provide valid credentials'})

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"Message"})
