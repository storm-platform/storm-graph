# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""A helper library in Python to persist iGraph graphs in JSON using the json-graph-specification"""

from .version import __version__
from .persistence import JSONGraphConverter

__all__ = ("__version__", "JSONGraphConverter")
