from rest_framework import viewsets
from .models import Park, Achievement, User, POI, UserAchievement, LoginSession, QRScan, Comment
from .serializers import ParkSerializer, AchievementSerializer, UserSerializer, POISerializer, UserAchievementSerializer, LoginSessionSerializer, QRScanSerializer, CommentSerializer

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
