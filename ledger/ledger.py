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
    if locale == 'en_US':
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
    elif locale == 'nl_NL':
        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = 0
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

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
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
