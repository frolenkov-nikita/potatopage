import os
from setuptools import setup


readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name     = 'potatopage',
    version  = '0.1',  # also update doc/conf.py:version
    packages = ['potatopage'],
    requires = ['python (>= 2.5)'],
    description  = 'Unified paginator',
    long_description = readme,
    author       = 'Anonymous',
    author_email = 'None',
    url          = 'https://github.com/potatolondon/potatopage',
    download_url = 'https://github.com/potatolondon/potatopage/archive/master.zip',
    license      = 'MIT License',
)