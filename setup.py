#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""The setup.py file."""

import os

from setuptools import find_packages, setup

URL = "https://github.com/RogerSelwyn/geniushub-client"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

VERSION = "0.8.0"

setup(
    name="geniushub-client",
    description="An aiohttp-based client for Genius Hub systems",
    keywords=["genius", "geniushub", "heatgenius"],
    author="Roger Selwyn",
    author_email="roger.selwyn@nomail.com",
    url=URL,
    install_requires=["aiohttp"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test", "docs"]),
    version=VERSION,
    license="MIT",
    python_requires=">=3.12.12",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.13",
        "Topic :: Home Automation",
    ],
    project_urls={  # Optional
        "Bug Reports": f"{URL}/issues",
        "Source": f"{URL}",
    },
)
