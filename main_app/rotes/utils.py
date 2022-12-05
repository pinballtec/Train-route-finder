from trains.models import Trains

def dfs_paths(graph, start, goal):
    """
    function for search of graphs with routes
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for i in qs:
        graph.setdefault(i.arrival_city_id, set())
        graph[i.arrival_city_id].add(i.departure_city_id)
    return(graph)


def get_routes(request, form) -> dict:
    """Implementing a graph search"""
    context = {'form': form}
    qs = Trains.objects.all()
    graph = get_graph(qs)
    "cleaning method for form"
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    traveling_time = data['traveling_time']
    cities = data['cities']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('Route not found')
    if cities:
        cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in cities):
                right_ways.append(route)
            if not right_ways:
                raise ValueError('This Route is not possible')
    return context

