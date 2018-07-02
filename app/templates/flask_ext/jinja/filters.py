from forex_python.converter import CurrencyCodes


def init_filters(app):
    @app.template_filter('currency_symbol')
    def currency_symbol_filter(currency_code):
        symbol = CurrencyCodes().get_symbol(currency_code)
        return symbol if symbol else '$'

    @app.template_filter('money')
    def money_filter(string):
        return '{:20,.2f}'.format(float(string))

    @app.template_filter('datetime')
    def simple_datetime_display(date):
        return date.strftime('%B %d, %Y %I:%M %p')
