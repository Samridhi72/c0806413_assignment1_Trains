def cal_trips(graph, fromnode, routes=[], single_route=[]):
    if fromnode in graph   :
        if len(single_route) > 2 and single_route[-1] == single_route[0] :
            temp = single_route[0]
            single_route = [temp]
        single_route.append(fromnode)
        for route in graph[fromnode]:
            if len(single_route) > 1 and single_route[0] == fromnode:
                print(single_route)
                routes.append(single_route)
                break

            cal_trips(graph, route, routes, single_route)
    return len(routes)





