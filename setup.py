#! /usr/bin/env python3
# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from setuptools import find_packages, setup

setup(
    name='surrogates',
    version='1.0.1',

    license='MIT',
    description='Encode and decode pairs of surrogate characters',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    url='https://github.com/hartwork/surrogates',

    install_requires=[
    ],
    tests_require=[
        'parameterized',
    ],

    packages=find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Text Processing',
    ],
)
