import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# =============================================================================
# Configure App
# =============================================================================

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "turkeyTwister451"

# =============================================================================
# Setup Database
# =============================================================================
db = SQLAlchemy(app=app)
Migrate(app,db)


# ----------- Run at command line for migrations -----------
# $ flask db init
# $ flask db migrate -m "<MESSAGE>"
# $ flask db upgrade
# ----------------------------------------------------------

