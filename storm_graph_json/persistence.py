# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph-json is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Graph Serializer."""

import json

from pydash import py_

from igraph import Graph
from typing import Dict, Union

from .schema import validate_schema


class JSONGraphConverter(object):
    """JSON Graph converter.

    Serializes/deserializes the igraph.Graph object into a JSON object.
    The JSON format used when reading/writing must follow the `json-graph-specification`.

    See:
        For more information about the `json-graph-specification`, please refer to the official documentation:
        https://github.com/jsongraph/json-graph-specification
    """

    @staticmethod
    def from_json(data: Dict) -> Union[Graph, None]:
        """Save a graph to a persistence store into a JSON file.

        Args:
            data (Dict): Dict in the `json-graph-specification` format that will be transformed into `igraph.Graph`.

        Returns:
            Union[igraph.Graph, None]: `igraph.Graph` loaded or None.

        See:
            For more information about the `json-graph-specitication`, please, see the
            official specification repository on the GitHub:
            https://github.com/jsongraph/json-graph-specification
        """
        # validating the json document schema
        validate_schema(data)

        # Extract data
        nodes = py_.get(data, "graph.nodes", {})
        edges = py_.get(data, "graph.edges", [])
        is_directed = py_.get(data, "graph.directed", False)

        # Rebuilding the `igraph.Graph` object
        g = Graph(directed=is_directed)

        # adding nodes
        for node_name in nodes:
            node_data = py_.get(nodes, node_name, {})
            node_metadata = py_.get(node_data, "metadata", {})

            g.add_vertex(name=node_name, **node_metadata)

        # adding edges
        for edge in edges:
            node_source_id = py_.get(edge, "source", None)
            node_target_id = py_.get(edge, "target", None)

            g.add_edge(
                node_source_id, node_target_id, metadata=py_.get(edge, "metadata", None)
            )
        return g

    @staticmethod
    def to_json(graph: Graph) -> Dict:
        """Transform a `igraph.Graph` in a JSON Document following the `json-graph-specification`.

        Args:
            graph (igraph.Graph): Graph to be saved.

        Returns:
            Dict: The transformed graph as dict.

        See:
            For more information about the `json-graph-specitication`, please, see the
            official specification repository on the GitHub:
            https://github.com/jsongraph/json-graph-specification
        """
        # add vertex
        nodes = {
            py_.get(node, "name"): {
                # converting attributes to avoid type errors
                "metadata": py_.omit(
                    json.loads(json.dumps(node.attributes(), default=str)), "name"
                )
            }
            for node in graph.vs
        }

        # add edges
        edges = py_.map(
            [
                {
                    "source": py_.get(graph.vs[edge.source], "name"),
                    "target": py_.get(graph.vs[edge.target], "name"),
                    "metadata": py_.get(edge, "metadata", None),
                }
                for edge in graph.es
            ],
            lambda x: {k: x[k] for k in x if x[k] is not None},
        )

        # creating the graph document
        graph_json = {
            "graph": {
                "directed": graph.is_directed(),
                "nodes": nodes if nodes else {},
                "edges": edges if edges else [],
            }
        }

        # validating the graph document
        validate_schema(graph_json)

        return graph_json


__all__ = "JSONGraphConverter"
