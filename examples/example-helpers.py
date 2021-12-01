# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import json
from storm_graph import graph_json_from_manager, graph_manager_from_json

#
# 1. Load example graph data
#
graph_data = json.load(open("data/graph.json"))


#
# 2. Create Graph Manager from JSON data
#
graph_manager = graph_manager_from_json(graph_data)

#
# 3. List vertices in the graph.
#
print("===")
for vertex in graph_manager.vertices:
    print(vertex.name)
    print(vertex)

#
# 4. Create Graph JSON (with `json-graph-specification`) from `GraphManager` data
#
graph_json = graph_json_from_manager(graph_manager)
print(json.dumps(graph_json))
