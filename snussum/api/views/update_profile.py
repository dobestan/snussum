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

        # 요청한 사용자의 닉네임이 현재 사용중인 닉네임인 경우
        if request.user.userprofile.nickname == nickname:
            return Response(status=status.HTTP_200_OK)

        # 다른 사용자가 이미 닉네임을 사용하고 있는 경우
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


class UpdateProfileGender(UpdateProfileBase):

    def put(self, request, *args, **kwargs):
        gender = request.data.get('gender')
        if gender == "boy":
            self.request.user.userprofile.is_boy = True
        if gender == "girl":
            self.request.user.userprofile.is_boy = False
        self.request.user.userprofile.save()
        return Response(status=status.HTTP_200_OK)


class UpdateProfileConditions(UpdateProfileBase):

    def put(self, request, *args, **kwargs):
        min_age = request.data.get('min_age', None)
        max_age = request.data.get('max_age', None)
        min_height = request.data.get('min_height', None)
        max_height = request.data.get('max_height', None)

        min_age = int(min_age) if min_age else None
        max_age = int(max_age) if max_age else None
        min_height = int(min_height) if min_height else None
        max_height = int(max_height) if max_height else None

        self.request.user.userprofile.update_conditions(
            is_dating_enabled=True,
            min_age=min_age,
            max_age=max_age,
            min_height=min_height,
            max_height=max_height,
        )

        return Response(status=status.HTTP_200_OK)


class ResetPassword(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        phonenumber = request.data.get('phonenumber', None)

        if email:
            user = User.objects.get(email=email)
        if phonenumber:
            user = User.objects.get(userprofile__phonenumber=phonenumber)

        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.userprofile.reset_password()
        return Response(status=status.HTTP_200_OK)
