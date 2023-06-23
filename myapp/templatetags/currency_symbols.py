from django import template

register = template.Library()

CURRENCY_SYMBOLS = {
    'USD': '$',
    'EUR': '€',
    # Add other currencies as needed
}

@register.filter(name='get_currency_symbol')
def get_currency_symbol(value):
    return CURRENCY_SYMBOLS.get(value, value)