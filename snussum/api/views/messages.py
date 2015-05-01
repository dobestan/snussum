from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.tasks.messages import send_sms, send_email


class APIMessageBase(APIView):
    permission_classes = (IsAuthenticated, )


class APIMessageSMS(APIMessageBase):

    def post(self, request, *args, **kwargs):
        send_sms.delay(request.data)
        return Response(status=status.HTTP_200_OK)


class APIMessageEmail(APIMessageBase):

    def post(self, request, *args, **kwargs):
        send_email.delay(request.data)
        return Response(status=status.HTTP_200_OK)
