# Graph_lab_1.py
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# Depth-first search, iterative
def dfs1(graph, start):
    visited, fringe = set(), [start]
    while fringe:
        vertex = fringe.pop() # Stack. Will take children, if they exist, over siblings because pop() grabs immediate expansion
        if vertex not in visited:
            visited.add(vertex)
            fringe.extend(graph[vertex] - visited) # Expand current node (i.e. put its children on the fringe and remove itself from fringe.)
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

# All paths DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                completePath = path + [next]
                #print "completePath: %s" % [completePath]
                yield completePath
            else:
                stack.append((next, path + [next]))

# Breadth-first search, iterative
def bfs(graph, start):
    visited, fringe = set(), [start]
    while fringe:
        vertex = fringe.pop(0) # Queue. Will take sibling, if they exist, over children as pop(0) looks for oldest member of queue.
        if vertex not in visited:
            visited.add(vertex)
            fringe.extend(graph[vertex] - visited) # Expand current node (i.e. put its children on the fringe and remove itself from fringe.)
    return visited
# End bfs

# All paths BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        #print "(vertex, path):"
        #print (vertex, path)
        for next in graph[vertex] - set(path):
            #print "next:"
            #print next
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
# End bfs_paths

# Shortest path BFS
def shortest_path_bf(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None
# End shortest_path

# Main
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

    # visitedBf = bfs(graph1, 'A')
    # print "Breadth-first search (bfs) visited:"
    # print visitedBf # i.e. All nodes in the graph

    pathsToGoal_bf = list(bfs_paths(graph1, 'A', 'F'))
    print "Paths to goal (bfs_paths):"
    print pathsToGoal_bf

    # shortestPathToGoal_bf = shortest_path_bf(graph1, 'A', 'F')
    # print "Shortest path to goal (shortest_path_bf):"
    # print shortestPathToGoal_bf

    # pathsToGoal_df = list(dfs_paths(graph1, 'A', 'F'))
    # print "Paths to goal (dfs_paths):"
    # print pathsToGoal_df

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

    # Print the graph
    # import DotVis
    # dotGraph = DotVis.undirDotGraph(graph1)
    # dotGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/DFS_intro_AI_4.gv', view=False)




