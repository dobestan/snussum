from django import template


register = template.Library()


@register.filter(name='partner')
def partner(dating, user):
    if not dating:
        return None

    if dating.boy == user:
        return dating.girl
    else:
        return dating.boy
