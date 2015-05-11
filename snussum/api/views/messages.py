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


class ContactAdmin(APIView):

    def post(self, request, *args, **kwargs):
        content = request.data.get("content", None)
        contact = request.data.get("contact", None)

        send_sms.delay({"to": "01022205736", "body": "%s from %s" % (content, contact)})

        if contact:
            send_sms.delay({
                'to': contact,
                'body': "[스누썸] 안녕하세요. 썸날입니다. 서비스에 문의사항/피드백을 남겨주셔서 진심으로 감사합니다.\
                        남겨주신 문의사항/피드백은 제가 확인 후 빠르게 연락드릴 수 있도록 하겠습니다. 감사합니다."
            })

        return Response(status=status.HTTP_200_OK)
