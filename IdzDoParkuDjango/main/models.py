import datetime
from django.db import models

class Park(models.Model):
    park_name = models.CharField(max_length=100)
    location = models.TextField()
    description = models.TextField()

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
    registration_date = models.DateField(default=datetime.datetime.now().date())
    score = models.IntegerField(default=0)

class POI(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    qr_code = models.TextField()
    additional_info_link = models.TextField()
    score_worth = models.IntegerField()

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

class LoginSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

class QRScan(models.Model):
    poi = models.ForeignKey(POI, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan_date = models.DateTimeField()

class Comment(models.Model):
    poi = models.ForeignKey(POI, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField()
