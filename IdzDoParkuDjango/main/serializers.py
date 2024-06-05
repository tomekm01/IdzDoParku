from rest_framework import serializers
from .models import Park, Achievement, User, POI, UserAchievement, LoginSession, QRScan, Comment
from django.contrib.auth.hashers import make_password

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
        extra_kwargs = {'password_hash': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password_hash'] = make_password(validated_data['password_hash'])
        return super(UserSerializer, self).create(validated_data)

class POISerializer(serializers.ModelSerializer):
    park = ParkSerializer()

    class Meta:
        model = POI
        fields = '__all__'

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
        fields = ['id', 'poi', 'user', 'content', 'comment_date']
        read_only_fields = ['id', 'poi', 'user', 'comment_date']
