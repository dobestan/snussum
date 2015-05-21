from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from random import randint


class Command(BaseCommand):
    help = 'Create demo user fixtures including superuser, in this case, "dobestan"'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # Create SuperUser
        user = User.objects.create_superuser(username="dobestan", password="dkstncks", email="dobestan@gmail.com")
        user.userprofile.is_university_verified = True
        user.userprofile.nickname = "dobestan"
        user.userprofile.is_boy = True
        user.userprofile.profile_introduce = "a" * 51
        user.userprofile.age = 23
        user.userprofile.height = 185
        user.userprofile.save()
        self.stdout.write('Successfully created superuser ...')

        # Create Boys
        for x in range(1, 19 + 1):
            user = User.objects.create_user(username="boy%02d" % x, password="dkstncks")
            user.userprofile.is_university_verified = True
            user.userprofile.nickname = "boy%02d" % x
            user.userprofile.is_boy = True
            user.userprofile.profile_introduce = "a" * 51
            user.userprofile.age = randint(20, 30)
            user.userprofile.height = randint(160, 190)
            user.userprofile.save()
        self.stdout.write('Successfully created boys ...')

        # Create Girls
        for y in range(1, 10 + 1):
            user = User.objects.create_user(username="girl%02d" % y, password="dkstncks")
            user.userprofile.is_university_verified = True
            user.userprofile.nickname = "girl%02d" % y
            user.userprofile.is_boy = False
            user.userprofile.profile_introduce = "a" * 51
            user.userprofile.age = randint(20, 30)
            user.userprofile.height = randint(145, 175)
            user.userprofile.save()
        self.stdout.write('Successfully created girls ...')
