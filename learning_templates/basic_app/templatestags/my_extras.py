from django import template

register = template.Library()

@register.filter(name='cut') # you can use this or the one on the 12th line
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)