import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-clikc-counter',
    version='0.0.1',
    packages=['django_clickcounter'],
    description='A Light django application with proper middleware to count clicks and opening an url without hitting database each time.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Execut3',
    author_email='execut3.binarycodes@gmail.com',
    url='https://github.com/Execut3/django-click-counter',
    license='GPT',
    install_requires=[
        'Django>=2.0',
    ],
    include_package_data=True,
)
