import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from django.contrib.auth.models import User

class NodeJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            print("No auth header or not Bearer format")
            return None

        token = auth_header.split(' ')[1]
        print("Got token:", token)

        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            print("Decoded payload:", payload)

        except jwt.ExpiredSignatureError:
            print("Token expired")
            raise exceptions.AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError as e:
            print("Token invalid:", e)
            raise exceptions.AuthenticationFailed('Invalid token')

        try:
            user = User.objects.get(id=payload['id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, token)
