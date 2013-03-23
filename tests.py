import os
import unittest
import tempfile

from adam import app, oid
from adam.cache import Cache
from adam.db import db_session, init_db
from adam.models import User

class AdamTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.test_client()
        init_db()

        db_session.add(User('Test User', 'test@example.com', 'testopenid'))
        db_session.commit()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    #

    def test_request_login(self):
        rv = self.app.get('/login')
        assert '<h3>Sign in</h3>' in rv.data

    def test_after_login(self):
        user = User.query.filter_by(openid='testopenid').first()
        assert user is not None

    def test_logout(self):
        rv = self.app.get('/logout', follow_redirects=True)
        assert 'You have been signed out' in rv.data

if __name__ == '__main__':
    unittest.main()
