from project import db
from project import login_manager
from werkzeug.security import (
    generate_password_hash,
    check_password_hash)
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    """
    # User
    
    Represents a user's profile
    """
    # MANUAL TABLE NAME CHOICE
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