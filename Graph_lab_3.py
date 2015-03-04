# Graph_lab_1.py
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# Depth-first search, iterative
def dfs1(graph, start):
    visited, fringe = set(), [start]

    #print "visited:"
    #print visited
    #print "fringe:"
    #print fringe

    while fringe:
        vertex = fringe.pop() # Stack
        #print "vertex: %s" % vertex
        if vertex not in visited:
            visited.add(vertex)
            #print "visited:"
            #print visited
            fringe.extend(graph[vertex] - visited) # Expand current node (i.e. put its children on the fringe and remove itself from fringe.)
            #print "fringe:"
            #print fringe
        # Iterate while, depth expansion. The author says this is recursive, but it's not. Nor does it backtrack. It just pops whatever is placed on the fringe, and therefor, as nodes expand their children go on the fringe and because it's a stack, pop emulates DFS.
    return visited
# End dfs1

# Depth-first search recursive.
# Diagnostic Example:
# start: A
# graph[start]: set(['C', 'B'])
# graph next: C
# graph[next]: set(['A', 'F'])
# next type: ['C']
# graph[next] type: [<type 'set'>]
def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited: # next is a child node in the set belonging to start.
        dfs2(graph, next, visited)
    return visited 
# End dfs2  

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                print "next: %s == goal: %s" % (next, goal)
                yield path + [next]
            else:
                stack.append((next, path + [next]))

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

    pathsToGoal = list(dfs_paths(graph1, 'A', 'F'))
    print "Paths to goal (dfs_paths):"
    print pathsToGoal

    # visited1A = dfs1(graph1, 'A')
    # print "Depth-first search (dfs1A) visited:"
    # print visited1A # i.e. All nodes in the graph

    # visited1C = dfs1(graph1, 'C')
    # print "Depth-first search (dfs1C) visited:"
    # print visited1C # i.e. All nodes in the graph

    # visited2A = dfs2(graph1, 'A')
    # print "Depth-first search (dfs2A) visited:"
    # print visited2A # i.e. All nodes in the graph

    # visited2C = dfs2(graph1, 'C')
    # print "Depth-first search (dfs2C) visited:"
    # print visited2C # i.e. All nodes in the graph

    # # Print the graph
    # import DotVis
    # dotGraph = DotVis.undirDotGraph(graph1)
    # dotGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/DFS_intro_AI_4.gv', view=False)




