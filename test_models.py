from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing users."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def testUserCreation(self):
        self.user = User(first_name='Jane', last_name='Doe', image_url='test_img_url')

        db.session.add(self.user)
        db.session.commit()

    def testFullName(self):
        self.assertEqual(self.user.full_name, 'Jane Doe')