#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup

setup(
    name="opencraft_courseware_search_filters",
    version="0.1.0",
    description="Custom search filters for Open edX LMS",
    author="OpenCraft",
    author_email="help@opencraft.com",
    url="https://github.com/open-craft/opencraft-courseware-search-filters",
    license="AGPL",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
    ],
    packages=["opencraft_courseware_search_filters"],
)
