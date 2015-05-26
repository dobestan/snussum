from django.core.urlresolvers import reverse

from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications import notify

from relationships.utils.hashids import get_encoded_dating_hashid

import datetime

from users.tasks.dating import send_dating_matched_sms

from snussum.settings import SNUSSUM_URL


class DatingManager(models.Manager):

    def datings(self):
        return Dating.objects.all()

    def datings_matched_today(self):
        return self.datings().filter(matched_at=datetime.date.today())

    def datings_matched_yesterday(self):
        return self.datings().filter(matched_at=datetime.date.today() - datetime.timedelta(1))


class Dating(models.Model):
    objects = DatingManager()

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
        if self.matched_at == datetime.date.today():
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

    def get_absolute_url(self):
        return reverse("dating-detail", kwargs={'slug': self.hash_id})

    def get_full_absolute_url(self):
        return SNUSSUM_URL + self.get_absolute_url()


@receiver(post_save, sender=Dating)
def _update_dating_hash_id(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_dating_hashid(instance.id)
        instance.save()

        # Notification
        notify.send(instance.girl, recipient=instance.boy,
                    action_object=instance, verb="created")
        notify.send(instance.boy, recipient=instance.girl,
                    action_object=instance, verb="created")

        # SMS
        send_dating_matched_sms(instance.boy, instance.girl, instance)
        send_dating_matched_sms(instance.girl, instance.boy, instance)
