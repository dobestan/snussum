from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from users.models.university import University


class UpdateProfileBase(APIView):
    permission_classes = (IsAuthenticated, )


class UpdateProfileUniversity(UpdateProfileBase):

    def put(self, request, *args, **kwargs):
        if not request.data.get('university', None) and \
                not request.data.get('username', None):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        university = University.objects.get(id=request.data.get('university'))
        email_username = request.data.get('username')

        self.request.user.userprofile.update_university(email_username, university)
        return Response(status=status.HTTP_200_OK)


class UpdateProfileNickname(UpdateProfileBase):

    def put(self, request, *args, **kwargs):
        nickname = request.data.get('nickname')
        if User.objects.filter(userprofile__nickname=nickname).first():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.request.user.userprofile.nickname = nickname
        self.request.user.userprofile.save()
        return Response(status=status.HTTP_200_OK)


class UpdateProfileIntroduce(UpdateProfileBase):

    def put(self, request, *args, **kwargs):
        introduce = request.data.get('introduce')
        self.request.user.userprofile.profile_introduce = introduce
        self.request.user.userprofile.save()
        return Response(status=status.HTTP_200_OK)
