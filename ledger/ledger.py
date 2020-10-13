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
    header_fmt = '{:10} | {:25} | {:13}'.format(*locale_opts['headers'])
    table = header_fmt
    entries = sorted(entries)
    while len(entries) > 0:
        table += '\n'

        # Find next entry in order
        min_entry_index = 0
        entry = entries[min_entry_index]
        entries.pop(min_entry_index)

        # Write entry date to table
        table += entry.date.strftime(locale_opts['date'])
        table += ' | '

        # Write entry description to table
        # Truncate if necessary
        if len(entry.description) > 25:
            for i in range(22):
                table += entry.description[i]
            table += '...'
        else:
            for i in range(25):
                if len(entry.description) > i:
                    table += entry.description[i]
                else:
                    table += ' '
        table += ' | '

        # Write entry change to table
        change_str = locale_opts['money'](entry.change, CURRENCY_SYMBOL[currency])
        while len(change_str) < 13:
            change_str = ' ' + change_str
        table += change_str
    return table
