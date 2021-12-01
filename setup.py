# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""A helper library in Python to persist iGraph graphs in JSON using the json-graph-specification"""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = []

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = []

install_requires = ["igraph>=0.9.8,<1", "jsonschema>=4.2.1,<4.5", "pydash>=5.1.0,<6.0"]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("storm_graph", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm-graph",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=[
        "Storm Platform",
        "Persistence",
        "json-graph-specification",
        "Helper Library",
    ],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-graph-json",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={},
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
