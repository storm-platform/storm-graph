# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from abc import ABC
from typing import Dict, List
from collections import UserDict

from .serializer import DictSerializable


class BaseGraphElement(UserDict, DictSerializable, ABC):
    """Base Graph element."""

    @property
    def metadata(self) -> Dict:
        return py_.get(self.data, "metadata", {})


class Vertex(BaseGraphElement):
    """Graph Vertex element."""

    def __init__(self, name: str, **kwargs):

        super(Vertex, self).__init__({"name": name, "metadata": kwargs or {}})

    @property
    def name(self) -> str:
        return py_.get(self.data, "name", None)

    @property
    def files(self) -> List:
        return py_.get(self.data, "metadata.files", [])

    def to_dict(self) -> Dict:
        return {self.name: self.metadata}


class Edge(UserDict):
    """Graph Edge element."""

    def __init__(self, source: str, target: str, **kwargs):
        super(Edge, self).__init__(
            {"source": source, "target": target, "metadata": {"metadata": kwargs or {}}}
        )

    @property
    def source(self) -> str:
        return py_.get(self.data, "source", None)

    @property
    def target(self) -> str:
        return py_.get(self.data, "target", None)

    @property
    def related_files(self) -> List:
        return py_.get(self.data, "metadata.related_files", [])

    def to_dict(self) -> Dict:
        return self.data


__all__ = ("Vertex", "Edge")
