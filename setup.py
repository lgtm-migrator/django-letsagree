#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : setup.py
#
#       Creation Date : Mon 08 Apr 2019 07:00:40 PM EEST (19:00)
#
#       Last Modified : Mon 05 Oct 2020 07:35:24 PM EEST (19:35)
#
# ==============================================================================

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-letsagree",
    version="1.1.8",
    python_requires=">=3.7",
    description=(
        "A django application that associates Groups with Terms "
        "requiring consent from logged in members."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/raratiru/django-letsagree",
    author="George Tantiras",
    license="BSD 3-Clause License",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["Django>=2.2", "django-translated-fields"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
