import typing
import math
import heapq


def sorted_edge_list_from_adjacency_list(adj):
    sorted_edge_list=[]
    for source_ind in adj:
        edge_dict = adj[source_ind]
        # print(source_ind, edge_dict)
        for target_ind in edge_dict:
            sorted_edge_list.append(tuple([edge_dict[target_ind], source_ind, target_ind]))

    sorted_edge_list.sort(key = lambda x:x[0])

    return sorted_edge_list


def parent(vertex_ind, parent_list):
    p = vertex_ind
    while parent_list[p] != -1:
        p = parent_list[p]

    return p


def kruskal(adjacency_list: dict) -> typing.Tuple[float, list]:
    # Weights should be positive (?)
    # edges are considered undirected

    n = len(adjacency_list) # Number of vertices
    tree_edge_list=[]
    mst_weight = 0

    # Setting all parents to -1 (Disjoint Set Union)
    parent_list = [-1 for i in range(n)]

    # Get the sorted edge list given the adjacency list (edge = (weight, source, target))
    sorted_edge_list = sorted_edge_list_from_adjacency_list(adjacency_list)

    for edge in sorted_edge_list:
        p1 = parent(edge[1], parent_list)
        p2 = parent(edge[2], parent_list)
        if p1 != p2:
            # Union operation
            parent_list[p2] = p1
            tree_edge_list.append([edge[1], edge[2]])
            mst_weight += edge[0]

    return mst_weight, tree_edge_list


def prim(adjacency_list):
    # This is very similar to Dijkstra's algorithm
    
    # Making all edges undirected
    for source_ind in adjacency_list:
        for target_ind in adjacency_list[source_ind]:
            if source_ind not in adjacency_list[target_ind]:
                adjacency_list[target_ind][source_ind] = adjacency_list[source_ind][target_ind]
            else:
                adjacency_list[target_ind][source_ind] = min(adjacency_list[target_ind][source_ind], adjacency_list[source_ind][target_ind])
    
    #
    n = len(adjacency_list)  # Number of vertices
    Q = [(0, 0)]
    min_weight_edge = {i: math.inf for i in range(n)}
    min_weight_edge[0] = 0
    parent = {i: -1 for i in range(n)}
    visited = set()
    mst_weight = 0

    while len(Q) > 0:
        v = heapq.heappop(Q)
        vertex_ind = v[1]

        if vertex_ind in visited:
            continue

        visited.add(vertex_ind)
        mst_weight += min_weight_edge[vertex_ind]

        # Updating min_edge_weight of all neighbour vertices of v
        for target_ind in adjacency_list[vertex_ind]:
            weight = adjacency_list[vertex_ind][target_ind]

            if min_weight_edge[target_ind] > weight:
                min_weight_edge[target_ind] = weight
                parent[target_ind] = vertex_ind
                heapq.heappush(Q, (min_weight_edge[target_ind], target_ind))

    return mst_weight, [[i, parent[i]] for i in range(1,len(parent))]


# example (even giving directed adjacency list should be fine, algo won't consider it)
adj_list = {0: {1: 1, 2: 1, 3: 3}, 1: {2: 2}, 2: {3: 1}, 3: {0: 4}}

print(kruskal(adj_list))
print(prim(adj_list))