from django.utils.deprecation import MiddlewareMixin
from blogApi.settings import PROTECTED_ROUTES
from blogApi.settings import JWT_CREDS
import jwt
from django.http import JsonResponse
import re

# Middleware for authorization.
class AuthorizationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def verify_jwt_token(self, token, secret_key, algorithm):
        try:
            decoded_payload = jwt.decode(token, secret_key, algorithms=algorithm)
            return decoded_payload
        except Exception as e:
            return False
        
    def checkProtectedRoute(self, path, _method):
        for route, method in PROTECTED_ROUTES:
            if re.match(route, path) and method == _method:
                return True
        return False
    

    def __call__(self, request):
        if self.checkProtectedRoute(request.path, request.method):
            jwt_token = request.headers.get('Authorization', None)
            payload = self.verify_jwt_token(jwt_token, JWT_CREDS["JWT_SECRET_KEY"], JWT_CREDS["ALGORITHM"])
            if not payload:
                return JsonResponse({"statusCode":401, "message":"Unauthorized"})
            request.jwt_payload = payload
        response = self.get_response(request)
        return response