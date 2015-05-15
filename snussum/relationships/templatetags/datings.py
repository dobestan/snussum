from django import template


register = template.Library()


@register.filter(name='partner')
def partner(dating, user):
    if dating.boy == user:
        return dating.girl
    else:
        return dating.boy


@register.filter(name="partner_is_accepted")
def partner_is_accepted(dating, user):
    if dating.boy == user:
        return dating.is_girl_accepted
    else:
        return dating.is_boy_accepted


@register.filter(name="myself_is_accepted")
def myself_is_accepted(dating, user):
    if dating.boy == user:
        return dating.is_boy_accepted
    else:
        return dating.is_girl_accepted
