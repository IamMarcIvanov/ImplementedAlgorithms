import typing
import math


class BellmanFordReturnVal:
    def __init__(self, parent, distances, negative_cycle_present):
        self.parent: typing.Dict[int,int] = parent
        self.distances: typing.Dict[int, float] = distances
        self.negative_cycle_present = negative_cycle_present

    def __repr__(self):
        rep = "Negative cycle exists: " + str(self.negative_cycle_present) + "\n"
        rep = rep + "Minimum distances\n" + str(self.distances) + "\n"
        rep = rep + "Parent structure\n" + str(self.parent) + "\n"

        return(rep)


def bellman_ford(adjacency_list: dict, source_vertex: int) -> BellmanFordReturnVal:
    # Negative edge weights allowed. Adj_list is of form {s_vertex: {t_vertex1: d1,...},...}
    # Will detect presence of a negative cycle, if present, 
    # will still give shortest paths to well defined shortest paths
    # Returns a dictionary of shortest path distances to all vertices from the specified vertex
    # Also returns a parent vertex list so that shortest paths can be reconstructed

    n: int = len(adjacency_list)  # Number of vertices
    distances: typing.Dict[int, float] = {i: math.inf for i in range(n)}
    distances[source_vertex] = 0
    parent: typing.Dict[int, int] = {i: -1 for i in range(n)}
    negative_cycle_present = False

    # Relaxing all edges n-1 times
    for i in range(n-1):
        # Iterating over all edges

        for source_ind in adjacency_list:
            for target_ind in adjacency_list[source_ind]:
                weight = adjacency_list[source_ind][target_ind]

                if distances[target_ind] > distances[source_ind] + weight:
                    distances[target_ind] = distances[source_ind] + weight
                    parent[target_ind] = source_ind

    # Checking for negative edges
    for i in range(1):
        # Iteration over all edges to check for negative cycles

        for source_ind in adjacency_list:
            for target_ind in adjacency_list[source_ind]:
                weight = adjacency_list[source_ind][target_ind]

                if distances[target_ind] > distances[source_ind] + weight:
                    negative_cycle_present = True
                    break

    retval: BellmanFordReturnVal = BellmanFordReturnVal(parent, distances, negative_cycle_present)

    return retval


# example
adj_list = {0: {1: -1, 2: 1, 3: 3, 4: 3}, 1: {2: 2}, 2: {3: 1}, 3: {}, 4: {5: 2}, 5: {4: -4}}
# This gives correct shortest paths for 0, 1, 2, 3

print(bellman_ford(adj_list, 0))