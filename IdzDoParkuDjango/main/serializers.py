from rest_framework import serializers
from .models import Park, Achievement, User, POI, UserAchievement, LoginSession, QRScan, Comment

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ('park_name',)

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class POISerializer(serializers.ModelSerializer):
    park = ParkSerializer()

    class Meta:
        model = POI
        fields = ('park', 'name', 'description', 'latitude', 'longitude', 'qr_code', 'additional_info_link', 'score_worth')

class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAchievement
        fields = '__all__'

class LoginSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginSession
        fields = '__all__'

class QRScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRScan
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
