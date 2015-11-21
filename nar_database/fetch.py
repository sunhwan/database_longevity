# fetch URLs
#
from bs4 import BeautifulSoup
import re
#from urllib import request
#from urllib.parse import urljoin, urlparse
from urllib import urlopen as request
from urlparse import urljoin, urlparse
import sys, os
import time
from sqlalchemy import create_engine

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'http://nar.oxfordjournals.org/content/32/suppl_1.toc'

# cache directory?
cache_dir = 'cache'
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# cache html files using issue number
def fetch(url):
    urlstring = urlparse(url)
    cachedfile = urlstring.path.replace('/', '_')
    if not os.path.exists('cache/%s' % cachedfile):
        content = request.urlopen(url).read().decode('utf-8')
        open('cache/%s' % cachedfile, 'w').write(content)
        time.sleep(2)
    return cachedfile
cachedfile = fetch(url)

# connect to database
from sqlalchemy import *
from model import Article
db = create_engine('sqlite:///nar.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db)
session = Session()

# parse and extract abstract URLs
db = create_engine('sqlite:///tutorial.db')
html = open('cache/%s' % cachedfile).read()
soup = BeautifulSoup(html, "html5lib")
elements = soup.find_all('a', rel='abstract')
for element in elements:
    uri = element.get('href')
    abstract_url = urljoin(url, uri)
    print(abstract_url)
    fetch(abstract_url)

    article = Article()
    article.url = abstract_url
    session.add(article)
session.commit()
