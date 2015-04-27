from django.contrib import admin

from relationships.models.dating import Dating


@admin.register(Dating)
class DatingAdmin(admin.ModelAdmin):
    pass
