#!/usr/bin/env python

import os
import sys

from threadfixproapi import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

# Publish helper
if sys.argv[-1] == 'build':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit(0)

if sys.argv[-1] == 'install':
    os.system('python setup.py sdist --formats=zip')
    sys.exit(0)
    
setup(
    name='threadfixproapi',
    packages=['threadfixproapi'],
    version=version,
    description='Python library enumerating the ThreadFix Professional RESTFul API.',
    long_description=readme,
    author='Brandon Spruth',
    author_email='brandon.spruth2@target.com',
    url='https://github.com/target/threadfixproapi',
    download_url='https://github.com/target/threadfixproapi/tarball/' + version,
    license='MIT',
    zip_safe=True,
    install_requires=['requests'],
    keywords=['threadfix', 'api', 'security', 'software', 'denim group', 'sast', 'dast'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.6',
    ]
)
