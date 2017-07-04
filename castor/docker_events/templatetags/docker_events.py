from django import template


register = template.Library()


@register.filter(name='get_attribute')
def get_attribute(value, arg):
    """
    Return the given requested attribute from the given Docker Event (value).

    Example event:

    {
        'Action': 'connect',
        'Actor': {
            'Attributes': {
                'container': 'c99c6a7810',
                'name': 'bridge',
                'type': 'bridge'
            },
            'ID': '3053f78c97'
        },
        'Type': 'network',
        'scope': 'local',
        'time': 1499164479,
        'timeNano': 1499164479075845726
    }
    """
    return value.get('Actor', {}).get('Attributes', {}).get(arg)
