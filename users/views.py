from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
import jwt
import datetime
from blogApi.settings import JWT_CREDS

# User registration by taking username, email, password.
@api_view(['POST'])
def registerUser(request):
    data = request.data
    username = data.get('username', None)
    email = data.get('email', None)
    password = data.get('password', None)

    if not (username and email and password):
        return JsonResponse({"statusCode":400, "response":"username, email, password are required"})
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return JsonResponse({'statusCode':200, 'response':'user registered'})
    except Exception as e:
        return JsonResponse({'statusCode':500, 'response':str(e)})

# Generates jwt token, if the user is already registered.
@api_view(['POST'])
def authenticate(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            payload = {
                "username": user.username,
                "id":user.pk,
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_CREDS["EXP_DURATION"])  # Token expires in 1 hour
            }
            token = jwt.encode(
                payload,
                JWT_CREDS["JWT_SECRET_KEY"],
                algorithm=JWT_CREDS["ALGORITHM"]
            )
            return Response({"message": token}, status=status.HTTP_200_OK)
        else:
            return  Response({"message": 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

