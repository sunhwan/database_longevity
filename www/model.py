from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///nar.db', echo=True)
Base = declarative_base()

class Article(Base):

    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Date)
    url = Column(String, unique=True, index=True)
    abstract = Column(String)
    doi = Column(String, unique=True, index=True)
    database_id = Column(Integer, ForeignKey('database.id'))

    def __init__(self):
        pass

class Database(Base):

    __tablename__ = "database"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String, index=True)
    is_alive = Column(Boolean)
    is_servicable = Column(Boolean)
    last_seen = Column(Date)

    def __init__(self):
        pass

if __name__ == "__main__":
    Base.metadata.create_all(engine)
