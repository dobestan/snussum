from django.contrib import admin

from relationships.models.dating import Dating
from relationships.models.self_dating import SelfDating, SelfDatingApply
from relationships.models.comment import Comment


@admin.register(Dating)
class DatingAdmin(admin.ModelAdmin):
    readonly_fields = ('matched_at',)


@admin.register(SelfDating)
class SelfDatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
