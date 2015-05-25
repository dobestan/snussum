from django.contrib import admin

from analytics.models.demographics import Demographics


@admin.register(Demographics)
class DemographicsAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )
    list_display = admin.ModelAdmin.list_display + (
        'users', 'boys', 'girls',
        'users_university_verified', 'boys_university_verified', 'girls_university_verified',
        'users_profile_verified', 'boys_profile_verified', 'girls_profile_verified',
    )
