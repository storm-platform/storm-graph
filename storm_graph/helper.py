# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from typing import Dict

from storm_graph.manager import GraphManager
from storm_graph.persistence import JSONGraphConverter


def graph_manager_from_json(json_obj: Dict, validate=True) -> GraphManager:
    """Create a graph manager based on a graph serialized as json object.

    Args:
        json_obj (Dict): Dict with a graph in the `json-graph-specification` schema.

        validate (boolean): Flag to enable the json schema validation.

    Returns:
        storm_graph.manager.GraphManager: GraphManager instance.

    See:
        For more information about the `json-graph-specification`, please refer to the official documentation:
        https://github.com/jsongraph/json-graph-specification
    """

    # parsing the json object as igraph.Graph
    graph_obj = JSONGraphConverter.from_json(json_obj, validate)

    return GraphManager(graph_obj)


def graph_json_from_manager(graph_manager: GraphManager, validate=True) -> Dict:
    """Create a graph serialized as json object from graph_manager.

    Args:
        graph_manager (storm_graph.manager.GraphManager): GraphManager instance.

        validate (boolean): Flag to enable the json schema validation.

    Returns:
        Dict: Dict with a graph in the `json-graph-specification` schema.

    See:
        For more information about the `json-graph-specification`, please refer to the official documentation:
        https://github.com/jsongraph/json-graph-specification
    """

    graph_obj = graph_manager.graph
    return JSONGraphConverter.to_json(graph_obj, validate)


__all__ = ("graph_json_from_manager", "graph_manager_from_json")
