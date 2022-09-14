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

from setuptools import find_packages, setup
setup(
    name='vlei',
    version='0.0.1',  # also change in src/vlei/__init__.py
    license='Apache Software License 2.0',
    description='Verifiable Legal Entity Identifier',
    long_description="Verifiable Legal Entity Identifier Schema Generator and Server",
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
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://keri.readthedocs.io/',
        'Changelog': 'https://keri.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/WebOfTrust/keripy/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.10.4',
    install_requires=[
                        'lmdb>=1.2.1',
                        'pysodium>=0.7.9',
                        'blake3>=0.2.0',
                        'msgpack>=1.0.2',
                        'cbor2>=5.4.1',
                        'multidict>=5.1.0',
                        'ordered-set>=4.1.0',
                        'hio>=0.5.8',
                        'multicommand>=0.1.1',
                        'jsonschema>=3.2.0',
                        'falcon>=3.0.1',
                        'daemonocle>=1.2.3',
                        'hjson>=3.0.2',
                        'PyYaml>=6.0',
                        'apispec>=5.1.1',
                        'mnemonic>=0.20',
                        'keri>=0.6.6',
    ],
    extras_require={
    },
    tests_require=[
                    'coverage>=5.5',
                    'pytest>=6.2.5',
                  ],
    setup_requires=[
    ],
    entry_points={
        'console_scripts': [
            'vLEI-generate = vlei.generate:main',
            'vLEI-server = vlei.server:main'
        ]
    },
)

