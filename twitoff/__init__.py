# this init file is the first thing to run
# whenever we launch the app
from .app import create_app

# this code starts the app automatically
APP = create_app()
# now we can run the app with a single flask
# run in the command line.