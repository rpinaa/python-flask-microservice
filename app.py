from flask import Flask
from flask_migrate import Migrate

from db import db
from schema import schema
from apis import api

app = Flask(__name__)

app.config.from_envvar('APP_CONFIG_FILE')

migrate = Migrate(app, db)

if __name__ == '__main__':
    db.init_app(app)
    schema.init_app(app)
    api.init_app(app)
    app.run()
