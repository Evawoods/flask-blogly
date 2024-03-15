from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
"""Models for Blogly."""

db = SQLAlchemy()

#Models go below:
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    first_name = db.Column(db.String(50),
                     nullable = False,
                     unique = False)
    
    last_name = db.Column(db.String(50),
                          nullable = False,
                          unique = False)
    
    image_url = db.Column(db.Integer,
                          nullable = False)
    
    @property
    def full_name(self):
        """Return full name of user"""

        return f"{self.first_name} {self.last_name}"
    
def connect_db(app):
    """Connect db to Flask app"""

    db.app = app
    db.init_app(app)