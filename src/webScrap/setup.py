import sys
import codecs
from setuptools import setup, find_packages

import webScrap

def long_description():
    with codecs.open('README.md', encoding='utf8') as f:
        return f.read()

setup(
    name='webScrap',
    version=webScrap.__version__,
    description=webScrap.__doc__.strip(),
    long_description=long_description(),
    author=webScrap.__author__,
    author_email='davearch@email.arizona.edu'
    license=webScrap.__licence__,
)
