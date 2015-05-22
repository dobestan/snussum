from django.contrib import admin

from relationships.models.dating import Dating
from relationships.models.self_dating import SelfDating, SelfDatingApply
from relationships.models.comment import Comment
from relationships.models.rating import Rating


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('created_at',)


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
    inlines = [CommentInline]


class SelfDatingApplyInline(admin.TabularInline):
    model = SelfDatingApply
    readonly_fields = ('created_at',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = admin.ModelAdmin.list_display + (
        'dating',
        'reviewer',
        'reviewee',
        'created_at',
        'score',
        'content',
    )


class RatingReviewerInline(admin.TabularInline):
    model = Rating
    readonly_fields = ('created_at', )
    fk_name = 'reviewer'


class RatingRevieweeInline(admin.TabularInline):
    model = Rating
    readonly_fields = ('created_at', )
    fk_name = 'reviewee'


@admin.register(SelfDating)
class SelfDatingAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'user', 'hash_id',
        'title',
        '_is_in_progress',
        'created_at', 'ends_at',
        'apply_count',
        'apply_is_accepted_count',
        'apply_is_not_accepted_count',
    )
    inlines = [SelfDatingApplyInline, ]
