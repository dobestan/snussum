from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

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
