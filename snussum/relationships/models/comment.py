from django.db import models

from django.contrib.auth.models import User
from relationships.models.dating import Dating

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify


class Comment(models.Model):
    user = models.ForeignKey(User)
    dating = models.ForeignKey(Dating)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Comment)
def _send_notifications(sender, instance, created, **kwargs):
    if created:
        if instance.user.userprofile.is_boy:
            partner = instance.dating.girl
        else:
            partner = instance.dating.boy

        if len(instance.content) < 30:
            content = instance.content
        else:
            content = instance.content[:30] + "..."

        notify.send(instance.user, recipient=partner, \
            action_object=instance, verb="created", \
            description=content)
