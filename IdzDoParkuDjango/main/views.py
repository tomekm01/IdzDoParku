from rest_framework import viewsets, generics
from .models import Park, Achievement, User, POI, UserAchievement, LoginSession, QRScan, Comment
from .serializers import ParkSerializer, AchievementSerializer, UserSerializer, POISerializer, UserAchievementSerializer, LoginSessionSerializer, QRScanSerializer, CommentSerializer
from django.contrib.auth import login, logout
from django.http import JsonResponse
import datetime
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
import json

class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class POIViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer

class UserAchievementViewSet(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class LoginSessionViewSet(viewsets.ModelViewSet):
    queryset = LoginSession.objects.all()
    serializer_class = LoginSessionSerializer

class QRScanViewSet(viewsets.ModelViewSet):
    queryset = QRScan.objects.all()
    serializer_class = QRScanSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=400)

        if check_password(password, user.password_hash):
            #login(request, user)
            
            login_session = LoginSession.objects.create(user=user, start_date=datetime.datetime.now(), end_date=datetime.datetime.now())
            
            return JsonResponse({'message': 'Login successful', 'session_id': login_session.id})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
