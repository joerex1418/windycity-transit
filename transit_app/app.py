import os

import functions as func
from constants import *

from flask import (
    Flask,
    url_for,
    request,
    jsonify,
    redirect,
    render_template,
    render_template_string)
from flask_login import LoginManager, UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

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

class User(db.Model):
    """
    # User
    Represents a user's profile
    """
    # MANUALLY SET TABLE NAME
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64),unique=True,index=True)
    loc_def = db.Column(db.Text)
    
    def __init__(self,name,username,password,email,loc_def):
        self.name = name
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email
        self.loc_def = loc_def
    
    def __repr__(self):
        return f"<model.User> NAME: {self.name} | USERNAME: {self.username} | EMAIL: {self.email}"

    def check_password(self,entered_password):
        return check_password_hash(self.password_hash,entered_password)

Migrate(app=app,db=db)
#       ----------- Run at command line for migrations -----------
#       $ flask db init
#       $ flask db migrate -m "<MESSAGE>"
#       $ flask db upgrade
#       ----------------------------------------------------------


# =============================================================================
# Routes
# =============================================================================
@app.route('/',methods=["GET","POST"])
def home():
    # print(db)
    # guest = User.query.get(1)
    # print(guest.check_password('password'))
    return render_template(
        'home.html',
        APP_TITLE=APP_TITLE)

@app.route('/tracking/nearme',methods=["GET","POST"])
def track_nearme():
    return render_template(
        'tracking_nearme.html',
        APP_TITLE=APP_TITLE)

@app.route('/tracking/data/nearme',methods=["GET","POST"])
def get_nearme_data():
    track_data = {
        "nearme":None
    }
    return jsonify(track_data)

@app.route('/tracking/cta',methods=["GET","POST"])
def track_cta():
    # if request.method == "POST":
    #     return "Hello"
    return render_template(
        'tracking_cta.html',
        # bus_stops = bus_rt_stops,
        # bus_routes = bus_routes,
        APP_TITLE = APP_TITLE)

@app.route('/tracking/data/cta',methods=["GET","POST"])
def get_cta_data():
    track_data = {
        "cta":None
    }
    return jsonify(track_data)

@app.route('/tracking/metra',methods=["GET","POST"])
def track_metra():
    return render_template(
        'tracking_metra.html',
        APP_TITLE=APP_TITLE)

@app.route('/tracking/data/metra',methods=["GET","POST"])
def get_metra_data():
    track_data = {
        "metra":None
    }
    return jsonify(track_data)

@app.route('/settings',methods=["GET","POST"])
def settings():
    return render_template(
        'settings.html',
        APP_TITLE=APP_TITLE)

@app.route('/get',methods=["GET","POST"])
def get():
    need = request.args.get("need")
    if need == "stops":
        search_by = request.args.get("search_by")
        route_id = request.args.get("route_id")
        direction = request.args.get("direction")
        stop_data = func.getStops(search_by,route_id=route_id,direction=direction)
        template_str = render_template('/blocks/ref-table.html',stop_data=stop_data)
        resp_data = {'data':stop_data,'html':template_str}
        return jsonify(resp_data)

host = "localhost"
host = "127.0.0.1"
if __name__ == "__main__":
    app.run(debug=True,host=host,port=5000)