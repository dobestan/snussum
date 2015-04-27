from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

from relationships.utils.hashids import get_encoded_dating_hashid


class Dating(models.Model):
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    boy = models.ForeignKey(User, related_name="dating_girls")
    girl = models.ForeignKey(User, related_name="dating_boys")

    matched_at = models.DateField(auto_now_add=True, blank=True)

    boy_checked_at = models.DateTimeField(blank=True, null=True)
    girl_checked_at = models.DateTimeField(blank=True, null=True)

    is_boy_accepted = models.BooleanField(default=False)
    is_girl_accepted = models.BooleanField(default=False)

    boy_accepted_at = models.DateTimeField(blank=True, null=True)
    girl_accepted_at = models.DateTimeField(blank=True, null=True)

    def _is_accepted(self):
        return self.is_boy_accepted and self.is_girl_accepted
    is_accepted = property(_is_accepted)

    class Meta:
        ordering = ['-matched_at']
        unique_together = (
            ("boy", "girl"),
        )

    def __str__(self):
        return "(%s, %s)" % (self.boy.username, self.girl.username)


@receiver(post_save, sender=Dating)
def _update_dating_hash_id(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_dating_hashid(instance.id)
        instance.save()
