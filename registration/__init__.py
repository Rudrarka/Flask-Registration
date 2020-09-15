from flask import Flask
from sqlalchemy import create_engine
from registration.db import Base
from sqlalchemy.orm import sessionmaker
import logging
import os

db_url = os.getenv('db_url')
app = Flask(__name__)
db_engine = create_engine(db_url, echo=True)
Base.metadata.create_all(bind=db_engine)
Session = sessionmaker(bind=db_engine)
logging.basicConfig(level=logging.DEBUG)


