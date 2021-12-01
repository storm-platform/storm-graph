# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from igraph import Graph
from copy import deepcopy

from .models import Vertex


class GraphManager:
    """Graph manager."""

    def __init__(self, graph=None):
        self._graph = graph or Graph(directed=True)

    @property
    def graph(self):
        """Create a deepcopy of the metadata graph instance."""
        return deepcopy(self._graph)

    @property
    def vertices(self):
        """Vertices in topological order."""
        for vertex_index in self._graph.topological_sorting(mode="out"):
            vertex = self._graph.vs[vertex_index]

            yield Vertex(**vertex.attributes())

    def _rebuild_graph(self) -> None:
        """Recreate the edges of the graph.

        Returns:
            None: The graph instance is inplace updated.
        """

        def _get_vertex_checksum(vertex_data, type):
            """Get vertex files checksum from defined metadata."""
            return set(
                py_.chain(vertex_data)
                .get("metadata.files", [])
                .filter_(lambda x: x.get("type") == type)
                .map(lambda x: py_.get(x, "checksum"))
                .value()
            )

        if len(self._graph.vs) > 1:  # If there is more than one node in the graph
            # rebuild the graph!

            # 1. Remove all edges
            self._graph.delete_edges()

            # 2. Rebuild edges
            for vertex_l1 in self._graph.vs:
                vertex_l1_files = _get_vertex_checksum(vertex_l1, "output")

                for vertex_l2 in self._graph.vs:
                    vertex_l2_files = _get_vertex_checksum(vertex_l2, "input")

                    if vertex_l1 != vertex_l2:
                        if not set(vertex_l2_files).isdisjoint(vertex_l1_files):
                            self._graph.add_edge(vertex_l1, vertex_l2)

    def add_vertex(self, vertex: Vertex):
        """Add vertex metadata to the graph.

        Args:
            vertex (storm_graph.models.graph.Vertex): Vertex object that will be added to graph.

        Returns:
            storm_graph.models.graph.Vertex: The added graph.
        """

        # Checks if the vertex exists
        current_vertex = None
        if self._graph:
            current_vertex = self._graph.vs.select(name=vertex.name)

        if current_vertex:
            graph_vertex = current_vertex[0]
            graph_vertex.update_attributes(**vertex.data)
        else:
            self._graph.add_vertex(**vertex.data)

        self._rebuild_graph()
        return vertex

    def delete_vertex(self, name: str, include_neighbors: bool = True) -> None:
        """Delete a metadata vertex from  graph.

        Args:
            name (str): Vertex name.

            include_neighbors (bool): Flag indicating whether the removed node's neighbors should also be
            considered for removal.

        Returns:
            None: The vertex is deleted inplace.
        """

        # Delete strategies
        def _delete_vertex_only(vtx):
            """Remove a specific vertex from the execution graph."""
            self._graph.delete_vertices(vtx)

        def _delete_neighborhood(vtx):
            """Remove all vertices subsequent to the one being removed."""
            neighborhood = self._graph.neighborhood(vtx, mode="out", order=10000)

            # deleting all vertices (including `vertex`)
            self._graph.delete_vertices(neighborhood)

        selected_vertex = None
        if self._graph:
            selected_vertex = self._graph.vs.select(name=name)

        if len(selected_vertex) == 1:
            vertex = selected_vertex[0]

            if include_neighbors:
                _delete_neighborhood(vertex)
            else:
                _delete_vertex_only(vertex)
            self._rebuild_graph()


__all__ = "GraphManager"
