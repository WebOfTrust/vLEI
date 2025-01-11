#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
$ python setup.py register sdist upload

First Time register project on pypi
https://pypi.org/manage/projects/


Pypi Release
$ pip3 install twine

$ python3 setup.py sdist
$ twine upload dist/keri-0.0.1.tar.gz

Create release git:
$ git tag -a v0.4.2 -m "bump version"
$ git push --tags
$ git checkout -b release_0.4.2
$ git push --set-upstream origin release_0.4.2
$ git checkout master

Best practices for setup.py and requirements.txt
https://caremad.io/posts/2013/07/setup-vs-requirement/
"""

from glob import glob
from os.path import basename
from os.path import splitext
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
if (this_directory / "README.md").exists():  # If building inside a container, like in the `container/Dockerfile`, this file won't exist and fails the build
    long_description = (this_directory / "README.md").read_text()
else:
    long_description = "Verifiable Legal Entity Identifier Schema Generator and Server"

setup(
    name='vlei',
    version='0.2.2',  # also change in src/vlei/__init__.py
    license='Apache Software License 2.0',
    description='Verifiable Legal Entity Identifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Samuel M. Smith',
    author_email='smith.samuel.m@gmail.com',
    url='https://github.com/WebOfTrust/vLEI',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://keri.readthedocs.io/',
        'Changelog': 'https://keri.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/WebOfTrust/keripy/issues',
    },
    keywords=[
        'keri','acdc','vlei'
    ],
    python_requires='>=3.12.2',
    install_requires=[
        'hio==0.6.14',
        'keri>=1.2.2',
        'falcon>=4.0.2',
        'multicommand>=1.0.0'
    ],
    extras_require={
    },
    tests_require=[
        'coverage>=7.6.10',
        'pytest>=8.3.4',
        'requests==2.32.3'
    ],
    setup_requires=[
        'setuptools==75.8.0'
    ],
    entry_points={
        'console_scripts': [
            'vLEI-generate = vlei.generate:main',
            'vLEI-server = vlei.server:main',
            'saidify-schema = vlei.saidify:main'
        ]
    },
)

