from django import template
register = template.Library()
def first_five_upper(value):
    result = value[:3].upper()
    return result
def first_n_upper(value,n):
    result = value[:2].upper()
    return result
register.filter('ffv',first_five_upper)
register.filter('fnu',first_n_upper)