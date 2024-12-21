from django import template

register = template.Library()


@register.filter
def currency(value, symbol='Rp'):
    """Format a number as currency."""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    return f"{symbol}{value:,.2f}"
