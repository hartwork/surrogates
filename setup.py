#! /usr/bin/env python3
# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from setuptools import find_packages, setup

setup(
    name='surrogates',
    version='1.0.2',

    license='MIT',
    description='Encode and decode pairs of surrogate characters',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    url='https://github.com/hartwork/surrogates',

    python_requires='>=3.5',
    setup_requires=[
        'setuptools>=38.6.0',  # for long_description_content_type
    ],
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Text Processing',
    ],
)
