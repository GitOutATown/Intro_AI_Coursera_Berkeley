# Graph_lab_1.py
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# Depth-first search
def dfs1(graph, start):
    visited, fringe = set(), [start]

    print "visited:"
    print visited
    print "fringe:"
    print fringe

    while fringe:
        vertex = fringe.pop() # Stack
        print "vertex: %s" % vertex
        if vertex not in visited:
            visited.add(vertex)
            print "visited:"
            print visited
            fringe.extend(graph[vertex] - visited) # Expand current node (i.e. put its children on the fringe and remove itself from fringe.)
            print "fringe:"
            print fringe
        # Iterate while, depth expansion. The author says this is recursive, but it's not. Nor does it backtrack. It just pops whatever is placed on the fringe, and therefor, as nodes expand their children go on the fringe and because it's a stack, pop emulates DFS.
    return visited

if __name__ == '__main__':
    # Graph
    graph1 = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }

    print "Graph:"
    print graph1

    visited = dfs1(graph1, 'A')
    print "Depth-first search visited:"
    print visited # i.e. All nodes in the graph

    import DotVis
    dotGraph = DotVis.undirDotGraph(graph1)
    dotGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/DFS_intro_AI_4.gv', view=False)




