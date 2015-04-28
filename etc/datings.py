from relationships.tasks.datings import match_all
from datetime import timedelta

# Suppose that user @dobestan is already created.

for x in range(9):
    user = User.objects.create(username="boy%s" % x)

for y in range(10):
    user = User.objects.create(username="girl%s" % y)
    user.userprofile.is_boy = False
    user.userprofile.save()

for z in range(10):
    match_all()
    for dating in Dating.objects.all():
        dating.matched_at -= timedelta(1)
        dating.save()
