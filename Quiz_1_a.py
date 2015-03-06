if __name__ == '__main__':
    # Graph

    graph1 = {
        'S': set(['D', 'A']),
        'A': set(['B', 'G']),
        'B': set(['C', 'E']),
        'C': set(['G']),
        'D': set(['B', 'E']),
        'E': set(['G'])
    }

    print "Graph:"
    print graph1

    import Graph_lab_4

    # Depth-first path
    pathsToGoal_df = list(Graph_lab_4.dfs_paths(graph1, 'S', 'G'))
    print "Paths to goal (dfs_paths):"
    print pathsToGoal_df

    # All paths BFS
    pathsToGoal_bf = list(Graph_lab_4.bfs_paths(graph1, 'S', 'G'))
    print "Paths to goal (bfs_paths):"
    print pathsToGoal_bf

    # Shortest path BFS
    shortestPathToGoal_bf = Graph_lab_4.shortest_path_bf(graph1, 'S', 'G')
    print "Shortest path to goal (shortest_path_bf):"
    print shortestPathToGoal_bf

    # Print the graph
    import DotVis
    dotGraph = DotVis.undirDotGraph(graph1)
    dotGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/Quiz_1_a.gv', view=False)
