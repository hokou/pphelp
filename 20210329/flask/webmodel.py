from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
# print(dir(db))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    username = db.Column(db.VARCHAR(255), nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password