from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify

from relationships.utils.hashids import get_encoded_dating_hashid

from datetime import date


class Dating(models.Model):
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    boy = models.ForeignKey(User, related_name="dating_girls")
    girl = models.ForeignKey(User, related_name="dating_boys")

    matched_at = models.DateField(auto_now_add=True, blank=True)

    boy_checked_at = models.DateTimeField(blank=True, null=True)
    girl_checked_at = models.DateTimeField(blank=True, null=True)

    is_boy_accepted = models.NullBooleanField()
    is_girl_accepted = models.NullBooleanField()

    boy_accepted_at = models.DateTimeField(blank=True, null=True)
    girl_accepted_at = models.DateTimeField(blank=True, null=True)

    boy_accepted_message = models.TextField(blank=True, null=True)
    girl_accepted_message = models.TextField(blank=True, null=True)

    def _is_accepted(self):
        return self.is_boy_accepted and self.is_girl_accepted

    _is_accepted.boolean = True
    is_accepted = property(_is_accepted)

    def pretty_date(self):
        if self.matched_at == date.today():
            return "오늘의 매칭"
        else:
            return "%s월 %s일" % (self.matched_at.month, self.matched_at.day)

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

        notify.send(instance.girl, recipient=instance.boy,
                    action_object=instance, verb="created")
        notify.send(instance.boy, recipient=instance.girl,
                    action_object=instance, verb="created")
