# extract url from an abstracts
#
from bs4 import BeautifulSoup
import re
import glob
import os
from datetime import datetime
from urlparse import urljoin, urlparse

_url = re.compile(r'((https?|ftp):\/\/)?[A-Za-z0-9\-_]+\.[A-Za-z0-9\~\/\-\._]+\/?')

# connect to database
from sqlalchemy import *
from model import *
db = create_engine('sqlite:///nar.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db)
session = Session()

ignore_urls = ['http://nar.oupjournals.org/']

for article in session.query(Article):
    urlstring = urlparse(article.url)
    abstract_fn = os.path.join('cache', urlstring.path.replace('/', '_'))

    if os.path.exists('exceptions/%s' % os.path.basename(abstract_fn)):
        abstract_fn = 'exceptions/%s' % os.path.basename(abstract_fn)
    print(abstract_fn)

    html = open(abstract_fn).read()
    soup = BeautifulSoup(html, "html5lib")
    title = soup.find('meta', attrs={'name': 'citation_title'}).get('content')
    doi = soup.find('meta', attrs={'name': 'citation_doi'}).get('content')
    date = soup.find('meta', attrs={'name': 'citation_date'}).get('content')
    try:
        author_email = soup.find('meta', attrs={'name': 'citation_author_email'}).get('content')
    except:
        author_email = ''
    e = soup.find('div', id='abstract-1')
    a = e.find('a')
    abstract = re.sub(r'\s+', ' ', e.find('p').text)

    if a is None:
        print(abstract_fn)
        #m = _url.search(abstract)
        #if m:
        #    url = m.group()
        #    if not (url.startswith('http') or url.startswith('ftp')): url = 'http://%s' % url
        #else:
        #    print(abstract_fn)
        break
    else:
        url = a.get('href')

    if url in ignore_urls: continue

    print title
    print doi
    print abstract
    print url

    article.title = title
    article.doi = doi
    article.year = datetime.strptime(date, '%m/%d/%Y')
    article.abstract = abstract

    q = session.query(Database).filter(Database.url == url).first()
    if q:
        database = q
    else:
        database = Database()
        database.title = title
        database.url = url
        session.add(database)

    article.database_id = database.id
    session.flush()

session.commit()
