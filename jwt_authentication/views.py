from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework import  status
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Successfully logged in', 'data': response.data}, status=status.HTTP_200_OK)