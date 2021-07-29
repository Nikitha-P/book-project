from flask import Flask, render_template, request,session,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from models import *
from app import app,db
import csv


engine=create_engine(os.getenv("DATABASE_URL"))
db_session=scoped_session(sessionmaker(bind=engine))
with open('books.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        new_book=Book(isbn=row[0], name=row[1],author=row[2],year=row[3])
        db_session.add(new_book)
db_session.commit()
db_session.close()