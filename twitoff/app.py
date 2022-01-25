# this is the app file, arguably the most
# important file in the app. We'll create
# our app object here and use it to detect
# when users are accessing specific pages
# and serve up HTML when they visit them.

from flask import Flask, render_template
from re import DEBUG
from .models import DB, User, Tweet

def create_app():
    # initialize the app
    app = Flask(__name__)

    # database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    '''We'll make a new route that detects
    when a user accesses it. We'll attach 
    each route to the app object.'''
    @app.route("/")
    def root():
        # return page contents
        return render_template(
            'base.html', title = 'home'
        )

    app_title = "Twitoff DS32"

    @app.route("/test")
    def test():
        return f"Another {app_title} page"

    @app.route("/hola")
    def hola():
        return "Hola, Twitoff!"

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return '''the database has been
        reset.'''
    
    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='julian')
        DB.session.add(julian)
        tweet1 = Tweet(id=1, text='tweet text', user=ryan)
        DB.session.add(tweet1)
        DB.session.commit()
        return '''Created some users'''
        
    return app