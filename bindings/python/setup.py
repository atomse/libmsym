#
#  setup.py
#  libmsym
#
#  Created by Marcus Johansson on 07/10/15.
#  Copyright (c) 2015 Marcus Johansson.
#
#  Distributed under the MIT License
#  ( See LICENSE file or copy at http://opensource.org/licenses/MIT )
#

import os
from setuptools import setup


def find_library(name):
    res = []
    for fname in os.listdir(name):
        if fname.endswith('.dylib'):
            res.append(fname)
        elif '.so' in fname:
            res.append(fname)
    return res


def get_version():
    import libmsym
    return libmsym.get_version()


setup(
    name='libmsym',
    version=get_version(),
    description='libmsym python binding',
    license='MIT',
    author='Marcus Johansson',
    author_email='mcodev31@gmail.com',
    url='https://github.com/mcodev31/libmsym',
    packages=['libmsym'],
    package_data={'': find_library('libmsym')},
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    platforms=["Linux", 'Darwin'],
    include_package_data=True,
    zip_safe=False,
)
