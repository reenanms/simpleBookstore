from config import *
import sqlalchemy
from entities.entityBase import *

def NewSession():
    engine = sqlalchemy.create_engine(CONNECTION_STRING)
    EntityBase.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    return Session()