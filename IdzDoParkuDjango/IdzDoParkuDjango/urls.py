"""
URL configuration for IdzDoParkuDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import ParkViewSet, AchievementViewSet, UserViewSet, POIViewSet, UserAchievementViewSet, LoginSessionViewSet, QRScanViewSet, CommentViewSet, RegisterUserView
from main.views import login_view, logout_view, get_user_info_view,get_user_achievements_view

router = DefaultRouter()
router.register(r'parks', ParkViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'users', UserViewSet)
router.register(r'pois', POIViewSet)
router.register(r'userachievements', UserAchievementViewSet)
router.register(r'loginsessions', LoginSessionViewSet)
router.register(r'qrscans', QRScanViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/get_user_info/', get_user_info_view, name='get_user_info'),
    path('api/get_user_achievements/', get_user_achievements_view, name='get_user_achievements'),
]
