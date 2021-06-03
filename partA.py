def cal_distance(edges):
# this assumes that there is a unique route selected from group 1( A-B-C)
    route = ['A', 'B', 'C']
    distance = 0
    for routestep in range(len(route)):
        startnode = route[routestep]
        if routestep+1 < len(route):
            endnode = route[routestep + 1]
            for edge in edges: #for iterating through available routes
                if edge[0] is startnode:
                    if edge[1] is endnode:
                        print(" fromnode: " + str(startnode))
                        print(" tonode: " + str(endnode))
                        print(" Distance b/w these nodes: " + str(edge[2]))
                        distance += edge[2]
                routestep += 1
    print("----- Total distance from A to C :  " + str(distance)+"  ------")
