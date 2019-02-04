# application entry point

import os

from flask_script import Manager

from app import create_app

app = create_app(os.getenv("APP_SETTING") or "production")

# instantiate manager with the flask instance
manager = Manager(app)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
