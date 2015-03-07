# Universal Cost Search

# Return path having least cost
def minCost(fringe):
    min = ()
    minCost = sys.maxsize
    newFringe = []
    for next in fringe:
        if next[2] < minCost:
            minCost = next[2]
            min = next
        else:
            newFringe.append(next)
    return (min, newFringe)

# Universal Cost Search with paths
def univ_cost_paths(graph, start, goal):
    fringe = [(start, [(start,0)], 0)] # vertex, path, accumulated cost
    while fringe:
        minCostRes = minCost(fringe)
        (vertex, path, cost) = minCostRes[0]
        fringe = minCostRes[1]
        for next in graph[vertex] - set(path):
            if next[0] == goal:
                completePath = path + [next]
                yield (completePath, cost + next[1])
            else:
                v = (next[0], path + [next], cost + next[1])
                fringe.append(v)

# As soon as we reach the goal the first time, we are done--it is the cheepest.
def cheepest_path_bf(graph, start, goal):
    try:
        return next(univ_cost_paths(graph, start, goal))
    except StopIteration:
        return None

# Main
if __name__ == '__main__':

    import sys
    
    # Graph
    graph1 = {
        'S': set([('D',2), ('A',3)]),
        'A': set([('B',5), ('G',10)]),
        'B': set([('C',2), ('E',1)]),
        'C': set([('G',4)]),
        'D': set([('B',1), ('E',4)]),
        'E': set([('G',3)])
    }

    print "Graph:"
    print graph1

    #print the graph
    import DotVis
    costGraph = DotVis.dirCostGraph(graph1)
    costGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/Quiz_1_cost.gv', view=False)
    #print costGraph

    pathsToGoal_ucs = list(univ_cost_paths(graph1, 'S', 'G'))
    print "Paths to goal (univ_cost_paths):"
    print pathsToGoal_ucs

    cheepestPathToGoal_bf = cheepest_path_bf(graph1, 'S', 'G')
    print "Cheepest path to goal (cheepest_path_bf):"
    print cheepestPathToGoal_bf




