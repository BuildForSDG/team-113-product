from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature,  SignatureExpired)
from src.app.models.base import Base
from src.app import db

class User(Base):
    __tablename__ = 'auth_user'
    public_id = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True)


    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    
    # def generate_auth_token(self, expiration=600):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)

    #     return s.dumps({'id': self.id})

    
    # @staticmethod
    # def verify_auth_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
        
    #     try:
    #         data = s.loads(token)
    #         user = User.query.get(data['id'])
    #         return user
        
    #     except SignatureExpired:
    #         return None
        
    #     except BadSignature:
    #         return None


    # def __repr__(self):
    #     return f'<User {self.first_name} {self.email}>'
