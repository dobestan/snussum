from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from users.models.university import University

from users.tasks.verification import snulife_login, mysnu_login


class VerifySNUBase(APIView):
    permission_classes = (IsAuthenticated, )


class VerifySNUSnulifeLogin(VerifySNUBase):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        result = snulife_login(username, password)
        if result:
            university = University.objects.get(slug="snu")
            self.request.user.userprofile.university = university
            self.request.user.userprofile.is_university_verified = True
            self.request.user.userprofile.snulife_username = username
            self.request.user.userprofile.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifySNUMysnuLogin(VerifySNUBase):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        result = mysnu_login(username, password)
        if result:
            university = University.objects.get(slug="snu")
            self.request.user.userprofile.university = university
            self.request.user.userprofile.is_university_verified = True
            self.request.user.userprofile.mysnu_username = username
            self.request.user.userprofile.save()

            self.request.user.email = username + "@snu.ac.kr"
            self.request.user.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifySNUMysnuEmail(VerifySNUBase):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        university = University.objects.get(slug="snu")

        self.request.user.userprofile.update_university(username, university)

        return Response(status=status.HTTP_200_OK)
