from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#from markdown import markdown
#import bleach
from flask import current_app, request, url_for
from sqlalchemy.orm import validates
#from flask_login import UserMixin, AnonymousUserMixin
#from app.exceptions import ValidationError
from . import db

class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8 
    ADMIN = 16

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    #password = db.Column(db.String(128))
    phone = db.Column(db.String(15))
    
    def __repr__(self):
        return '<User {}>'.format(self.username) 
    
    
    def set_password(self, password):
        if not password:
            raise AssertionError('Password not provided')
        
        # if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
        #     raise AssertionError('Password must contain 1 capital letter and 1 number')
        
        if len(password) < 8 or len(password) > 50:
            raise AssertionError('Password must be between 8 and 50 characters')
        
        self.password_hash = generate_password_hash(password) 
        
        
    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
    
    
    @validates('username') 
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
            
        if User.query.filter(User.username == username).first():
            raise AssertionError('Username is already in use')
            
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters') 
            
        return username 
    
    
    @validates('email')     
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        
        # if not re.match("[^@]+@[^@]+\.[^@]+", email):
        #     raise AssertionError('Provided email is not an email address')
          
        return email