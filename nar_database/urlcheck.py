# check if the URL is active
#
from urllib import urlopen as request
from urlparse import urlparse
import httplib

# connect to database
from sqlalchemy import *
from model import *
db = create_engine('sqlite:///nar.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db)
session = Session()

def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    try:
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
        return resp.status
    except:
        return False

for database in session.query(Database):
    code = checkUrl(database.url)
    #if code:
    #    if code == 200:
    #        database.is_alive = True
    #        database.is_servicable = True
    #    elif code < 400:
    #        database.is_alive = True
    #        database.is_servicable = True
    #else:
    #    database.is_alive = False
    #    database.is_servicable = False

    print database.url, database.is_alive, code
    #session.flush()

#session.commit()
