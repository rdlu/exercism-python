import json
from collections import defaultdict

class RestAPI:
    def __init__(self, database:dict=None):
        self._database = defaultdict(list)
        self._database.update(database)

    def get(self, url: str, payload: str = '[]') -> str:
        if url == '/users':
            decoded_payload = json.loads(payload)['users']
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
            return self._database['users'] 
        return [ user for user in self._database['users'] if user['name'] in user_list ]

    def _add_user(self, user_info: dict) -> dict:
        if user_info['user']:
            self._database['users'].append(
                {"name": user_info['user'], "owes": {}, "owed_by": {}, "balance": 0.0})
            return self._filter_users([user_info['user']])[0]
        return {}

    def _iou_user(self, users_info: dict) -> dict:
        lender = self._filter_users(users_info['lender'])[0]
        borrower = self._filter_users(users_info['borrower'])[0]
        amount = users_info['amount']
        if lender and borrower:
            lender['owed_by'][borrower['name']] = amount
            lender['balance'] += amount
            borrower['owes'][lender['name']] = amount
            borrower['balance'] -= amount
            return {'users': self._filter_users([borrower['name'], lender['name']])}
        else:
            return {}
