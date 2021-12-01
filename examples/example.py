# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import json
from storm_graph import JSONGraphConverter

#
# 1. Load example graph data
#
graph_data = json.load(open("data/graph.json"))

#
# 2. Parse the loaded graph to iGraph.Graph
#
igraph_obj = JSONGraphConverter.from_json(graph_data)
print(igraph_obj)

#
# 3. From iGraph.Graph to JSON
#
igraph_json = JSONGraphConverter.to_json(igraph_obj)
print(igraph_json)
