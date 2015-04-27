from django.db import models

from django.contrib.auth.models import User


class Dating(models.Model):
    boy = models.ForeignKey(User, related_name="dating_girls")
    girl = models.ForeignKey(User, related_name="dating_boys")

    class Meta:
        unique_together = (
            ("boy", "girl"),
        )

    def __str__(self):
        return "(%s, %s)" % (self.boy.username, self.girl.username)
