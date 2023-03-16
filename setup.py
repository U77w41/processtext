"""setup"""
import pathlib
import os
import codecs
from setuptools import setup

HERE = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
__version__ = '0.0.1'
__maintainer__ = 'Ujjwal Chowdhury'


# Setting up
setup(
    name='processtext',
    version=__version__,
    description='An open-source python package to process text data',
    author=__maintainer__,
    author_email='<u77w41@gmail.com>',
    url='https://github.com/U77w41/processtext',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['processtext'],
    install_requires=['nltk','re','autocorrect','string'],
    tests_require=['pytest'],
    keywords= ['python','nlp','text','regex', 'text processing']
)
