from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify

from relationships.utils.hashids import get_encoded_self_dating_hashid

from django.contrib.auth.models import User

from datetime import timedelta, datetime


class SelfDating(models.Model):
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)
    user = models.ForeignKey(User)

    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(default=None, blank=True, null=True)

    tags_myself = ArrayField(models.CharField(max_length=8), blank=True)
    tags_partner = ArrayField(models.CharField(max_length=8), blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("self-dating-detail", kwargs={'slug': self.hash_id})

    def _time_left(self):
        if self.is_finished:
            return None
        time_left_in_timedelta = self.ends_at - datetime.now()
        return {
            'days': time_left_in_timedelta.days,
            'hours': time_left_in_timedelta.seconds // 3600,
            'minutes': time_left_in_timedelta.seconds // 60 % 60,
        }
    time_left = property(_time_left)

    def _is_finished(self):
        return datetime.now() > self.ends_at
    is_finished = property(_is_finished)


class SelfDatingApply(models.Model):
    self_dating = models.ForeignKey(SelfDating)
    user = models.ForeignKey(User)

    content = models.TextField()

    class Meta:
        unique_together = (
            ("self_dating", "user"),
        )

    def get_absolute_url(self):
        return reverse("self-dating-detail", kwargs={'slug': self.self_dating.hash_id})


@receiver(post_save, sender=SelfDating)
def _update_self_dating(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_self_dating_hashid(instance.id)

        if not instance.ends_at:
            instance.ends_at = instance.created_at + timedelta(3)

        instance.save()
