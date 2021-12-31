from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from config import DevApplicationConfiguration
from db import db
from resources.routes import routes

app = Flask(__name__)
app.config.from_object(DevApplicationConfiguration)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
api = Api(app)
[api.add_resource(*r) for r in routes]



if __name__ == "__main__":
    app.run()
