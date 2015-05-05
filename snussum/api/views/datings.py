from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from relationships.models.dating import Dating


class DatingComment(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        dating = Dating.objects.get(hash_id=self.kwargs['hash_id'])
        return Response(status=status.HTTP_200_OK)
