import typing
import heapq
import math

def dijkstra(adjacency_list: typing.Dict[int, typing.Dict], source_vertex: int) -> typing.Tuple[typing.Dict[int, float], typing.Dict[int,int]]:
    # No negative edge weights allowed. Adj_list is of form {s_vertex: {t_vertex1: d1,...},...}
    # Returns a dictionary of shortest path distances to all vertices from the specified vertex
    # Also returns a parent vertex list so that shortest paths can be reconstructed

    n: int = len(adjacency_list)  # Number of vertices
    min_distance: typing.List[typing.Tuple] = [(0,source_vertex)]
    distances: typing.Dict[int, float] = {i: math.inf for i in range(n)}
    distances[source_vertex] = 0
    parent: typing.Dict[int, int] = {i: -1 for i in range(n)}
    visited: typing.Set[int] = set()

    while len(min_distance) > 0:
        v: typing.Tuple = heapq.heappop(min_distance)
        vertex_ind = v[1]

        if vertex_ind in visited:
            continue

        visited.add(vertex_ind)

        # Relaxing all edges of vertex v
        for target_ind in adjacency_list[vertex_ind]:
            weight = adjacency_list[vertex_ind][target_ind]

            if distances[target_ind] > distances[vertex_ind] + weight:
                distances[target_ind] = distances[vertex_ind] + weight
                parent[target_ind] = vertex_ind
                heapq.heappush(min_distance, (distances[target_ind], target_ind))

    return distances, parent

# example
adj_list = {0: {1: 1, 2: 1, 3: 3}, 1: {2: 2}, 2: {3: 1}, 3: {}}
print(dijkstra(adj_list, 0))


