from re import A
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Profile
from django.contrib.auth import logout, login
from .serializers import EventSerializer, ProfileSerializer, UserCreateAccount
from rest_framework.authtoken.models import Token
# Create your views here.



class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):  # sourcery skip: extract-method
        serializer = UserCreateAccount(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'succesfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
            



class ProfileViewGet(APIView):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
class ProfileViewUpdate(APIView):
    def patch(self, request,pk, *args, **kwargs):
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(instance=profile,data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

class EventViewGet(APIView):
    def get(self,request,*args,**kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
class EventViewPost(APIView):
    def post(self,request,*args,**kwargs):
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

class EventViewUpdate(APIView):
    def put(self,request,id,*args,**kwargs):
        event = Event.objects.get(id=id)
        serializer = EventSerializer(instance=event,data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class EventViewDelete(APIView):
    def delete(self,request,id,*args,**kwargs):
        event = Event.objects.get(id=id)
        events = Event.objects.all()
        event.delete()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
        
# class LogoutUsers(APIView):
#     def get(self,request,*args,**kwargs):
#         acc = request.user.auth_token.delete()
#         logout(request,acc)
#         return Response('User Logged out successfully')
    
class LogoutUsers(APIView):
    def get(self,request,*args,**kwargs):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message":"Logged out successfully"})
    
def home(request):
    return render(request,'index.html')