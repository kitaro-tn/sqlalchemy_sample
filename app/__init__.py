from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Model = declarative_base()

class Session():

    def __init__(self):
        engine = create_engine('mysql+pymysql://root@localhost/gochiusa?charset=utf8', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
