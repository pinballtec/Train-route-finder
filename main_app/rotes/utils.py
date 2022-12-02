from trains.models import Trains

def get_graph(qs):
    graph = {}
    for i in qs:
        graph.setdefault(i.from_city_id, set())
        graph[i.from_city_id].add(i.to_city_id)
    return(graph)

def get_routes(request, form) -> dict:
    qs = Trains.objects.all()
    graph = get_graph(qs)