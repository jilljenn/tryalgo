#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
Setup file
"""

from pathlib import Path
from setuptools import setup
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='tryalgo',
    version='1.5.0',
    description=(
        'Algorithms and data structures '
        'for preparing programming competitions'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jill-Jênn Vie and Christoph Dürr',
    author_email='christoph.durr@lip6.fr',
    license='MIT',
    url='https://jilljenn.github.io/tryalgo/',
    keywords='algorithms data-structures programming competition',
    packages=['tryalgo'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
