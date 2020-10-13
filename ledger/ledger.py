# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None

    def __lt__(self, other):
        return (self.date, self.change, self.description) < (other.date, other.change, other.description)


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


LOCALES = {
    'en_US': {
        'headers': ['Date', 'Description', 'Change'],
        'date': '%m/%d/%Y',
        'money': lambda cents, symbol: (lambda value: f'({value})' if cents < 0 else f'{value} ')
                                       (f'{symbol}{abs(cents)/100:,.2f}')
    },
    'nl_NL': {
        'headers': ['Datum', 'Omschrijving', 'Verandering'],
        'date': '%d-%m-%Y',
        'money': lambda cents, symbol: f'{symbol} {cents/100:_.2f} '.replace('.', ',').replace('_', '.')

    }
}

CURRENCY_SYMBOL = {
    'USD': '$',
    'EUR': '€'
}


def format_entries(currency, locale, entries):
    locale_opts = LOCALES[locale]
    header = '{:10} | {:25} | {:13}'.format(*locale_opts['headers'])

    def row_fmt(entry):
        date = entry.date.strftime(locale_opts['date'])
        description = entry.description[:22] + '...' if len(entry.description) > 25 else entry.description
        change = locale_opts['money'](entry.change, CURRENCY_SYMBOL[currency])
        return '{:10} | {:25} | {:>13}'.format(date, description, change)

    rows = [row_fmt(entry) for entry in sorted(entries)]
    return '\n'.join([header, *rows])
