import os
import sys

from setuptools import setup, find_packages

from stompest import FULL_VERSION

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

if sys.version_info[:2] < (2, 7):
    print 'stompest requires Python version 2.7 or later (%s detected).' % '.'.join(sys.version_info[:2])
    sys.exit(-1)
if sys.version_info[:2] >= (3, 0):
    print 'stompest is not yet compatible with Python 3 (%s detected).' % '.'.join(sys.version_info[:2])
    sys.exit(-1)

setup(
    name='stompest',
    version=FULL_VERSION,
    author='Jan Mueller',
    author_email='nikipore@gmail.com',
    description='STOMP library for Python including a synchronous client.',
    license='Apache License 2.0',
    packages=find_packages(),
    namespace_packages=['stompest'],
    long_description=read('README.txt'),
    keywords='stomp activemq rabbitmq apollo',
    url='https://github.com/nikipore/stompest',
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    tests_require=['mock'],
    test_suite='stompest.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Twisted',
        'Topic :: System :: Networking',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
