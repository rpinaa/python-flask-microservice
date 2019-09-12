from flask import Flask
from flask_migrate import Migrate

from data_source import dataSource
from schema import schema
from apis import api

app = Flask(__name__)

app.config.from_envvar('APP_CONFIG_FILE')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

migrate = Migrate(app=app, db=dataSource)

if __name__ == '__main__':
    dataSource.init_app(app)
    schema.init_app(app)
    api.init_app(app)
    app.run()
