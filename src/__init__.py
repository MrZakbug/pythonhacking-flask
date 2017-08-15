import os

from flask import Flask

from src.database import db_session, init_engine, init_db


app = Flask(__name__)
app.config.from_object('src.default_settings')
if 'LOCAL_SETTINGS' in os.environ:
    app.config.from_envvar('LOCAL_SETTINGS')

init_engine(app.config['DATABASE_URI'])
init_db()

import src.views


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
