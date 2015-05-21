from relationships.tasks.datings import match_all
from datetime import timedelta

from random import randint

user = User.objects.create_superuser(username="dobestan", password="dkstncks", email="dobestan@gmail.com")
user.userprofile.nickname = "dobestan"
user.userprofile.is_boy = True
user.userprofile.profile_introduce = "a" * 51
user.userprofile.age = 23
user.userprofile.height = 185
user.userprofile.save()

for x in range(9):
    user = User.objects.create_user(username="boy%s" % x, password="dkstncks")
    user.userprofile.nickname = "boy%2s" % x
    user.userprofile.is_boy = True
    user.userprofile.profile_introduce = "a" * 51
    user.userprofile.age = randint(20, 30)
    user.userprofile.height = randint(160, 190)
    user.userprofile.save()

for y in range(10):
    user = User.objects.create_user(username="girl%s" % y, password="dkstncks")
    user.userprofile.nickname = "girl%2s" % y
    user.userprofile.is_boy = False
    user.userprofile.profile_introduce = "a" * 51
    user.userprofile.age = randint(20, 30)
    user.userprofile.height = randint(145, 175)
    user.userprofile.save()

for z in range(10):
    match_all()
    for dating in Dating.objects.all():
        dating.matched_at -= timedelta(1)
        dating.save()
