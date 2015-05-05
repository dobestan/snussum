from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from relationships.models.dating import Dating
from relationships.models.comment import Comment


class DatingComment(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        dating = Dating.objects.get(hash_id=self.kwargs['hash_id'])

        if self.request.user not in [dating.boy, dating.girl]:
            return Response(status=status.HTTP_403_FORBIDDEN)

        comment = \
            Comment.objects.create(user=self.request.user, dating=dating, content=request.data.get('content'))

        data = {
                'content': comment.content,
        }

        return Response(status=status.HTTP_201_CREATED, data=data)
