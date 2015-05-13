from django.db import models

from django.contrib.auth.models import User
from relationships.models.dating import Dating


class Rating(models.Model):
    dating = models.ForeignKey(Dating)

    reviewer = models.ForeignKey(User, related_name="rating_reviewees")
    reviewee = models.ForeignKey(User, related_name="rating_reviewers")

    class Meta:
        unique_together = (
            ("reviewer", "reviewee"),
            ("reviewee", "reviewer"),
        )
