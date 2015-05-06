#!/usr/bin/env python
import codecs
import os
import re
from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts), encoding='utf8').read()

setup(
    name='recordpeeker',
    description='Peeks at data from FFRK',
    long_description=read('README.md'),
    version='0.1.9',
    packages=find_packages(),
    author='Jonathan Chang',
    url='https://github.com/jonchang/recordpeeker',
    license='MIT',
    install_requires=[
        'mitmproxy>=0.11.3',
        'tabulate>=0.7.5',
        'requests>=2.7'
    ],
    include_package_data=True,
    package_data={
        'recordpeeker': ["data/*.csv"]
        },
    entry_points={
      'console_scripts':[
          'recordpeeker=recordpeeker.command_line:launch',
          'forever24=recordpeeker.bin.command_line:launch'
      ]
   }
)


