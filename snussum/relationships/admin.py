from django.contrib import admin

from relationships.models.dating import Dating
from relationships.models.self_dating import SelfDating, SelfDatingApply
from relationships.models.comment import Comment


@admin.register(Dating)
class DatingAdmin(admin.ModelAdmin):
    readonly_fields = ('matched_at',)
    list_display = admin.ModelAdmin.list_display + (
        'boy', 'girl',
        'matched_at',
        '_is_accepted',
        'is_boy_accepted',
        'is_girl_accepted',
    )


class SelfDatingApplyInline(admin.TabularInline):
    model = SelfDatingApply
    readonly_fields = ('created_at',)


@admin.register(SelfDating)
class SelfDatingAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'user', 'hash_id',
        'title',
        '_is_in_progress',
        'created_at', 'ends_at',
    )
    inlines = [SelfDatingApplyInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
