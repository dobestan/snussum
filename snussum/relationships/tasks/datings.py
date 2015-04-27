from users.models.user_profile import UserProfile
from relationships.models.dating import Dating


def match_all():
    bigger_group, smaller_group = UserProfile.objects.divide_groups()

    for user in smaller_group:
        match_user_in_smaller_group(user, bigger_group)


def match_user_in_smaller_group(user, bigger_group):
    for partner in bigger_group:
        if user.userprofile.is_dating_available_with(partner):
            return user.userprofile.create_dating_with(partner)
