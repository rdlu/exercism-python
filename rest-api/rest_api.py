import json
from collections import defaultdict

class User(object):
    def __init__(self, name, owed_by=None, owes=None, **kwargs):
        self.name = name
        self.records = {}
        for borrower, amount in (owed_by or {}).items():
            self.loan(borrower, amount)
        for lender, amount in (owes or {}).items():
            self.borrow(lender, amount)

    def borrow(self, borrower, amount):
        self.records[borrower] = self.records.get(borrower, 0) - amount

    def loan(self, lender, amount):
        self.records[lender] = self.records.get(lender, 0) + amount

    @property
    def owes(self):
        return {k: -v for k, v in self.records.items() if v < 0}

    @property
    def owed_by(self):
        return {k: v for k, v in self.records.items() if v > 0}

    @property
    def balance(self):
        return sum(self.records.values())

    @property
    def __dict__(self):
        return {
            'name': self.name,
            'owes': self.owes,
            'owed_by': self.owed_by,
            'balance': self.balance
        }

class RestAPI:
    def __init__(self, database:dict=None):
        self._database = {
            user['name']: User(**user)
            for user in (database or {}).get('users', [])
        }

    def get(self, url: str, payload: str = '{}') -> str:
        if url == '/users':
            decoded_payload = json.loads(payload).get('users', [])
            response = self._filter_users(decoded_payload)
            return json.dumps({'users': response})
        else:
            return ''

    def post(self, url:str, payload:str=''):
        decoded_payload = json.loads(payload)
        if url == '/add':
            return json.dumps(self._add_user(decoded_payload))
        elif url == '/iou':
            return json.dumps(self._iou_user(decoded_payload))
        else:
            return ''

    def _filter_users(self, user_list: list) -> list:
        if not user_list:
            return list(self._database.values())
        return [ user.__dict__
                for name, user in sorted(self._database.items())
                if name in user_list ]

    def _add_user(self, user_info: dict) -> dict:
        user = User(user_info['user'])
        self._database[user.name] = user
        return user.__dict__

    def _iou_user(self, users_info: dict) -> dict:
        lender = self._database[users_info['lender']]
        borrower = self._database[users_info['borrower']]
        amount = users_info['amount']
        if lender and borrower:
            lender.loan(borrower.name, amount)
            borrower.borrow(lender.name, amount)
            return {'users': sorted(
                [lender.__dict__, borrower.__dict__],
                key=lambda u: u['name']
            )}
        return {'users': []}
