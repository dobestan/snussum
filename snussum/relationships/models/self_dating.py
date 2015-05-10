from django.db import models

from django.contrib.auth.models import User


class SelfDating(models.Model):
    user = models.ForeignKey(User)


class SelfDatingApply(models.Model):
    dating = models.ForeignKey(SelfDating)
    user = models.ForeignKey(User)
