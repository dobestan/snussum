from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify

from relationships.utils.hashids import get_encoded_self_dating_hashid

from django.contrib.auth.models import User

from datetime import timedelta


class SelfDating(models.Model):
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user.username


class SelfDatingApply(models.Model):
    dating = models.ForeignKey(SelfDating)
    user = models.ForeignKey(User)


@receiver(post_save, sender=SelfDating)
def _update_self_dating(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_self_dating_hashid(instance.id)

        if not instance.ends_at:
            instance.ends_at = instance.created_at + timedelta(3)

        instance.save()
