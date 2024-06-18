from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from .models import Park, Achievement, User, POI, UserAchievement, LoginSession, QRScan, Comment, UserPOI
from .serializers import ParkSerializer, AchievementSerializer, UserSerializer, POISerializer, UserAchievementSerializer, LoginSessionSerializer, QRScanSerializer, CommentSerializer, UserPOISerializer
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.core.serializers import serialize
import datetime
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
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

class UserPOIViewSet(viewsets.ModelViewSet):
    queryset = UserPOI.objects.all()
    serializer_class = UserPOISerializer

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
            
            login_session = LoginSession.objects.create(user=user, start_date=datetime.datetime.now())

            return JsonResponse({'message': 'Login successful', 'session_id': login_session.id})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)

        try:
            login_session = LoginSession.objects.get(id=session_id, end_date__isnull=True)
            login_session.end_date = datetime.datetime.now()
            login_session.save()
            return JsonResponse({'message': 'Logout successful'})
        except LoginSession.DoesNotExist:
            return JsonResponse({'message': 'Invalid session ID'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def get_user_info_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        
        try:
            login_session = LoginSession.objects.get(id=session_id)
            user_id = login_session.user.pk
            username = login_session.user.username
            score = login_session.user.score
            return JsonResponse({'message': 'Get user info successful', 'user_id': user_id, 'username': username, 'score': score})
        except LoginSession.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def get_user_achievements_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        
        try:
            login_session = LoginSession.objects.get(id=session_id)
            users_ach = UserAchievement.objects.filter(user=login_session.user).select_related('achievement')
            #users_ach = Achievement.objects.filter(id__in=users_ach_id).values()
            achievements = [ua.achievement for ua in users_ach]
            serialized_achievements = AchievementSerializer(achievements, many=True).data
            #serialized_ach = serialize("json", users_ach)
            #serialized_ach = json.loads(serialized_ach)
            #all_ach = Achievement.objects.values()
            #data = {}
            #for e in all_ach:
            #    if e.id not in users_ach_id:
                    
            return JsonResponse({'message': 'Get user achievements successful', 'serialized_achievements': serialized_achievements})
        except LoginSession.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def get_user_ranking(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        
        try:
            #login_session = LoginSession.objects.get(id=session_id)
            user_ranking = User.objects.all().order_by('-score').values()
            serialized_ranking = UserSerializer(user_ranking, many=True).data

            return JsonResponse({'message': 'Get user ranking successful', 'serialized_ranking': serialized_ranking})
        except LoginSession.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def check_qr_code(request, poi_id):
    if request.method == "POST":
        data = json.loads(request.body)
        qr_code = data.get("qr_code")
        poi = get_object_or_404(POI, id=poi_id)
        if poi.qr_code == qr_code:
            return JsonResponse({"valid": True})
        return JsonResponse({"valid": False})
    
def get_comments(request, poi_id):
    comments = Comment.objects.filter(poi_id=poi_id)
    serialized_comments = CommentSerializer(comments, many=True).data
    return JsonResponse(serialized_comments, safe=False)


#@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_comment(request, poi_id):
    try:
        data = request.data
        session_id = data.get('session_id')
        if not session_id:
            return Response({'error': 'session_id is required'}, status=400)

        # Find the login session
        try:
            login_session = LoginSession.objects.get(id=session_id, end_date__isnull=True)
            user = login_session.user
        except LoginSession.DoesNotExist:
            return Response({'error': 'Invalid session ID'}, status=404)

        # Find the POI
        try:
            poi = POI.objects.get(id=poi_id)
        except POI.DoesNotExist:
            return Response({'error': 'POI not found'}, status=404)

        # Create and save the comment
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            # Log przed zapisem
            print(f"Creating comment for POI ID {poi_id} by user {user.username}")

            # Zapis komentarza
            serializer.save(poi=poi, user=user, comment_date=datetime.datetime.now())

            # Log po zapisie
            print("Comment created successfully")
            
            return Response(serializer.data, status=201)
        else:
            # Log błędów walidacji
            print("Validation errors:", serializer.errors)

            return Response(serializer.errors, status=400)
    except Exception as e:
        # Log ogólnego wyjątku
        print("Exception:", str(e))
        return Response({'error': str(e)}, status=500)
