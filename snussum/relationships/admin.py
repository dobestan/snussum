from django.contrib import admin

from relationships.models.dating import Dating
from relationships.models.comment import Comment


@admin.register(Dating)
class DatingAdmin(admin.ModelAdmin):
    readonly_fields = ('matched_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
