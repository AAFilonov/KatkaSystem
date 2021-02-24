from unittest import TestCase, skip
from mock import patch
import itertools

from application.api.v1_0.user import get_user, get_users


class Test(TestCase):
    @skip
    def test_get_user(self):

        usr_json = get_users()
        print(usr_json)
        self.assertEqual(usr_json, '')

    @skip
    def test_get_user_by_id(self):
        usr_json = get_user(1)
        print(usr_json)
        self.assertEqual(usr_json, '')
