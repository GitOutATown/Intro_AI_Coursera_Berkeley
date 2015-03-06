# Universal Cost Search

def univ_cost_paths(graph, start, goal):
    queue = [(start, [(start,0)])]
    while queue:
        ##print "queue:"
        #print queue
        (vertex, path) = queue.pop(0)
        #print "(vertex, path):"
        #print (vertex, path)
        #print "expansion for %s:" % [vertex]
        #print graph[vertex]
        for next in graph[vertex] - set(path):
            #print "next:"
            #print next
            pathPlusNext = path + [next]
            #print "path + [next]:"
            #print pathPlusNext
            if next[0] == goal:
                completePath = path + [next]
                #print "completePath: %s" % [completePath]
                yield completePath
            else:
                #print "appending to queue:"
                #print (next[0], path + [next])
                queue.append((next[0], path + [next]))

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




