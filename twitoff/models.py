'''SQLAlchemy user and tweet models for our
database.'''
from flask_sqlalchemy import SQLAlchemy

# creates a DB object (similar to our
# cursor in regular sql.)
DB = SQLAlchemy()

# making a user table using sqlalchemy
class User(DB.Model):
    # id column
    id = DB.Column(
        DB.BigInteger, primary_key = True
    )
    # name column
    username = DB.Column(DB.String,
    nullable = False)

    def __repr__(self):
        return "<User: {}>".format(
            self.username)

class Tweet(DB.Model):
    '''Keeps track of tweets for every
    user.'''
    id = DB.Column(DB.BigInteger,
        primary_key = True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger,
        DB.ForeignKey('user.id'),
        nullable = False)
    user = DB.relationship('User',
        backref = DB.backref('tweets',
        lazy = True))
    
    def __repr__(self):
        return "Tweet: {}".format(
            self.text
        )
'''Run repl with FLASK_APP=app flask shell,
this will allow us to interact with our DB
as if it was in a production environment.'''
