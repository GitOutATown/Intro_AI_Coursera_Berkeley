# My Dot GraphVis utility. Converts a Python format to Dot

# Example of expected format:
# graph1 = {
#     'A': set(['B', 'C']),
#     'B': set(['A', 'D', 'E']),
#     'C': set(['A', 'F']),
#     'D': set(['B']),
#     'E': set(['B', 'F']),
#     'F': set(['C', 'E'])
# }

from graphviz import Graph

def isDuplicate(placed, edge):
    for placedEdge in placed:
        if placedEdge == edge:
            return True
    return False

def undirDotGraph(graph):
    g = Graph()
    placed = set([])
    for key in graph:
        for neighbor in graph[key]:
            edge = frozenset([key, neighbor]) # Hashing set of sets
            if not isDuplicate(placed, edge):
                g.edge(key, neighbor)
                placed.add(edge)
    return g
