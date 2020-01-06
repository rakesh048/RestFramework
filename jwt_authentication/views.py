from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken, RefreshJSONWebToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import RegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response("User registered Successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Successfully logged in', 'data': response.data},
                        status=status.HTTP_200_OK)


class RefreshToken(RefreshJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(RefreshToken, self).post(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Refresh token send Successfully', 'data': response.data},
                        status=status.HTTP_200_OK)


class VerifyToken(VerifyJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(VerifyToken, self).post(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Token verify Successfully', 'data': response.data},
                        status=status.HTTP_200_OK)
