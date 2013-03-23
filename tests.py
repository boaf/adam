import os
import adam
import unittest
import tempfile

class AdamTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, adam.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = adam.app.test_client()
        adam.db.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(adam.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()
