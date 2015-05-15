from django.db import models

from django.contrib.auth.models import User
from relationships.models.dating import Dating


class Rating(models.Model):
    dating = models.ForeignKey(Dating)

    reviewer = models.ForeignKey(User, related_name="rating_reviewees")
    reviewee = models.ForeignKey(User, related_name="rating_reviewers")

    SCORE_CHOICES = (
        (4.3, "A+"),
        (4.0, "A0"),
        (3.7, "A-"),

        (3.3, "B+"),
        (3.0, "B0"),
        (2.7, "B-"),

        (2.3, "C+"),
        (2.0, "C0"),
        (1.7, "C-"),

        (1.3, "D+"),
        (1.0, "D0"),
        (0.7, "D-"),

        (0.0, "F"),
    )
    score = models.IntegerField(choices=SCORE_CHOICES, default=None, blank=True, null=True)
    content = models.TextField(default=None, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ("reviewer", "reviewee"),
            ("reviewee", "reviewer"),
        )
