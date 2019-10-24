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

from setuptools import setup


setup(
    name='libmsym',
    version='0.2.4',
    description='libmsym python binding',
    license='MIT',
    author='Marcus Johansson',
    author_email='mcodev31@gmail.com',
    url='https://github.com/mcodev31/libmsym',
    packages=['libmsym'],
    package_data={'': ['libmsym.so', 'libmsym.so.0.2', 'libmsym.so.0.2.4']},
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    platforms=["Linux"],
    include_package_data=True,
    zip_safe=False,
)
