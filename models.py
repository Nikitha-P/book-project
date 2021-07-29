from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Register(db.Model):
    __tablename__="registration"
    name=db.Column(db.String, primary_key=True)
    mail=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)

class Book(db.Model):
    __tablename__="book"
    isbn=db.Column(db.String, primary_key=True)
    title=db.Column(db.String, nullable=False)
    author=db.Column(db.String, nullable=False)
    year=db.Column(db.Integer, nullable=False)
