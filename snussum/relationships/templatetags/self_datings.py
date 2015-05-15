from django import template


register = template.Library()


@register.filter(name="myself_dating_apply")
def myself_dating_apply(self_dating, user):
    return self_dating.selfdatingapply_set.filter(user=user).first()
