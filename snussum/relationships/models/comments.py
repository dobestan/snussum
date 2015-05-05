from django.db import models

from django.contrib.auth.models import User
from relationships.models.dating import Dating


class Comment(models.Model):
    user = models.ForeignKey(User)
    dating = models.ForeignKey(Dating)

    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
