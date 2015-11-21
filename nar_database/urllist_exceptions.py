# list of abstracts that we can't easily extract URLs
#
from bs4 import BeautifulSoup
import re, os
import glob

for abstract_fn in glob.glob('cache/*.abstract'):
    html = open(abstract_fn).read()
    soup = BeautifulSoup(html, "html5lib")
    e = soup.find('div', id='abstract-1')
    a = e.find('a')
    abstract = e.find('p').text
    if a is None:
        print(abstract_fn)
        if not os.path.exists('exceptions/%s' % os.path.basename(abstract_fn)):
            os.system('cp %s exceptions/%s' % (abstract_fn, os.path.basename(abstract_fn)))
