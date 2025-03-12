from .db import db, environment, SCHEMA
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, plain_password):
        self._password = plain_password
    
    def to_dict(self):
        return {
            'id': self.id,
            'userName': self.user_name,
            'email': self.email,
            'password': self._password,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }