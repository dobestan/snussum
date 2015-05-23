from django.core.urlresolvers import reverse
from django.db import models

from django.contrib.auth.models import User
from relationships.models.dating import Dating

from relationships.utils.hashids import get_encoded_comment_hashid

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify


class Comment(models.Model):
    hash_id = models.CharField(max_length=16, unique=True, blank=True, null=True)

    user = models.ForeignKey(User)
    dating = models.ForeignKey(Dating)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("dating-detail", kwargs={'slug': self.dating.hash_id}) + "#" + self.hash_id


@receiver(post_save, sender=Comment)
def _send_notifications(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_comment_hashid(instance.id)
        instance.save()

        if instance.user.userprofile.is_boy:
            partner = instance.dating.girl
        else:
            partner = instance.dating.boy

        notify.send(instance.user, recipient=partner,
                    action_object=instance, verb="created",
                    description=instance.content)
