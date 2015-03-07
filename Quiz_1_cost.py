# Universal Cost Search

def univ_cost_paths(graph, start, goal):
    fringe = [(start, [(start,0)])]
    while fringe:
        print "fringe TOP:"
        print fringe
        (vertex, path) = fringe.pop(0)
        print "(vertex, path):"
        print (vertex, path)
        print "expansion for %s:" % [vertex]
        print graph[vertex]
        print "set(path):"
        print set(path)
        print "graph[vertex] - set(path):"
        print graph[vertex] - set(path)
        print "fringe::"
        print fringe
        for next in graph[vertex] - set(path):
            print "fringe:::"
            print fringe
            print "next:"
            print next
            print "graph[vertex]:"
            print graph[vertex]
            pathPlusNext = path + [next]
            print "path + [next]:"
            print pathPlusNext
            if next[0] == goal:
                completePath = path + [next]
                print "completePath: %s" % [completePath]
                yield completePath
            else:
                print "===> path + [next]:"
                print path + [next]
                print "fringe before appending next tupple"
                print fringe
                print "appending to fringe:"
                print (next[0], path + [next])
                fringe.append((next[0], path + [next]))
                print "---> fringe BOTTOM:"
                print fringe

if __name__ == '__main__':
    
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

    # print the graph
    import DotVis
    costGraph = DotVis.dirCostGraph(graph1)
    costGraph.render('/Users/hieronymus/Development/Courses/edX/Artificial Intelligence/Python/labs/Quiz_1_cost.gv', view=False)
    #print costGraph

    pathsToGoal_ucs = list(univ_cost_paths(graph1, 'S', 'G'))
    print "Paths to goal (univ_cost_paths):"
    print pathsToGoal_ucs




