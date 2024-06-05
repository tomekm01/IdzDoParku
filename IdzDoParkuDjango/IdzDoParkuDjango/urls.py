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
from main.views import login_view, check_qr_code, get_comments, add_comment

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
    path('api/pois/<int:poi_id>/check_qr_code/', check_qr_code, name='check_qr_code'),
    path('api/pois/<int:poi_id>/comments/', get_comments, name='get_comments'),
    path('api/pois/<int:poi_id>/add_comment/', add_comment, name='add_comment'),
]
