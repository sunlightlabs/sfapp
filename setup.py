from setuptools import setup, find_packages
import os

from sfapp import __version__

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='sfapp',
    version=__version__,
    description='Django app for Sunlight Foundation mini-app wrapper',
    long_description=readme,
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    url='http://github.com/sunlightlabs/sfapp/',
    packages=find_packages(),
    package_data={
        'sfapp': [
            'static/*/css/*',
            'static/*/js/*',
            'static/*/img/*',
            'templates/*/*',
        ]
    },
    license='BSD License',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
