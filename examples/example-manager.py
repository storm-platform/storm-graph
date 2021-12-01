# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from storm_graph import GraphManager
from storm_graph.models import Vertex

#
# 1. Create the graph manager.
#
graph_manager = GraphManager()


#
# 2. Add vertices to the graph.
#

# adding vertex (1) to the vertex.
vertex_1 = Vertex(
    "wt410zkq75",
    files=[
        {
            "type": "input",
            "key": "input.txt",
            "checksum": "d4d910d7bd5644a34d12c109731c815b",
        },
        {
            "type": "output",
            "key": "output.txt",
            "checksum": "4a9dbcab0a169bf7c9a6db65d5c069d9",
        },
    ],
)
print(vertex_1.files)

# adding the created vertex to the graph.
graph_manager.add_vertex(vertex_1)

# adding vertex (2) to the vertex.
vertex_2 = Vertex(
    "tw041qkz57",
    files=[
        {
            "type": "input",
            "key": "output.txt",
            "checksum": "4a9dbcab0a169bf7c9a6db65d5c069d9",  # same as defined in the "vertex_1 output" file
        },
        {
            "type": "output",
            "key": "output.txt",
            "checksum": "8d1600210acf94c2619850b0ae8c8c25",
        },
    ],
)
print(vertex_2.files)

# adding the created vertex to the graph.
graph_manager.add_vertex(vertex_2)

#
# 3. List vertices in the graph.
#
print("===")
for vertex in graph_manager.vertices:
    print(vertex.name)
    print(vertex)

#
# 4. Delete vertex.
#
graph_manager.delete_vertex("tw041qkz57")  # defined in the `vertex_2` variable.

#
# 5. List vertices in the graph (again).
#
print("===")
for vertex in graph_manager.vertices:
    print(vertex.name)
    print(vertex)
