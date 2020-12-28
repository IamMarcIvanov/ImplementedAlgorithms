import typing
import math
import copy


def floyd_warshall(adjacency_matrix: list) -> list:
    # Adjacency matrix should be given, if weight of edge(u,v) = w then adj_mat[u][v] = w
    # If edge(u,v) does not exist, then adj_mat[u][v] = math.inf
    # edge(u,u) should be 0
    # Returns a dictionary of shortest path distances to all vertices from the specified vertex
    
    distances = copy.copy(adjacency_matrix)
    n = len(adjacency_matrix)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                distances[u][v] = min(distances[u][v], distances[u][k] + distances[k][v])

    return distances


# example
adj_mat = [[0, 2, 1, 3],
           [math.inf, 0, 1, math.inf],
           [math.inf, math.inf, 0, 1],
           [4 ,math.inf, math.inf, 0]]

print(floyd_warshall(adj_mat))