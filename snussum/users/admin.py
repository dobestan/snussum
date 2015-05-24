from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from users.models.user_profile import UserProfile
from users.models.university import University

from relationships.admin import SelfDatingApplyInline, RatingReviewerInline, RatingRevieweeInline


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    inline_classes = ('grp-collapse grp-open',)


class UserAdmin(UserAdmin):
    list_display = [
        'username',
        'nickname',
        'hash_id',
        'is_boy',
        'is_profile_verified',
        'is_dating_enabled',
        'email',
        'is_university_verified',
        'mysnu_username',
        'snulife_username',
        'phonenumber',
        'is_phonenumber_verified',
        'age',
        'height',
        'age_condition',
        'height_condition',
    ]

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline, SelfDatingApplyInline, RatingReviewerInline, RatingRevieweeInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)

    def hash_id(self, obj):
        return obj.userprofile.hash_id

    def is_boy(self, obj):
        return obj.userprofile.is_boy
    is_boy.boolean = True

    def is_dating_enabled(self, obj):
        return obj.userprofile.is_dating_enabled
    is_dating_enabled.boolean = True

    def is_profile_verified(self, obj):
        return obj.userprofile.is_profile_verified
    is_profile_verified.boolean = True

    def nickname(self, obj):
        return obj.userprofile.nickname

    def phonenumber(self, obj):
        return obj.userprofile.phonenumber

    def is_phonenumber_verified(self, obj):
        return obj.userprofile.is_phonenumber_verified
    is_phonenumber_verified.boolean = True

    def is_university_verified(self, obj):
        return obj.userprofile.is_university_verified
    is_university_verified.boolean = True

    def mysnu_username(self, obj):
        return obj.userprofile.mysnu_username

    def snulife_username(self, obj):
        return obj.userprofile.snulife_username

    def age(self, obj):
        return obj.userprofile.age

    def height(self, obj):
        return obj.userprofile.height

    def age_condition(self, obj):
        if obj.userprofile.age_condition:
            return "(%s, %s)" % (obj.userprofile.age_condition.lower, obj.userprofile.age_condition.upper)

    def height_condition(self, obj):
        if obj.userprofile.height_condition:
            return "(%s, %s)" % (obj.userprofile.height_condition.lower, obj.userprofile.height_condition.upper)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
