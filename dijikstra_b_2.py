import operator
from WeightedGraph import Graph, Vertex


def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path


# Program to find shortest paths from vertex A.
g = Graph()

vertex_s = Vertex("S")
vertex_a = Vertex("A")
vertex_b = Vertex("B")
vertex_c = Vertex("C")
vertex_d = Vertex("D")
vertex_e = Vertex("E")
vertex_f = Vertex("F")
vertex_g = Vertex("G")
vertex_h = Vertex("H")
vertex_i = Vertex("I")
vertex_j = Vertex("J")
vertex_k = Vertex("K")
vertex_l = Vertex("L")


g.add_vertex(vertex_s)
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)
g.add_vertex(vertex_f)
g.add_vertex(vertex_g)
g.add_vertex(vertex_h)
g.add_vertex(vertex_i)
g.add_vertex(vertex_j)
g.add_vertex(vertex_k)
g.add_vertex(vertex_l)

g.add_undirected_edge(vertex_s, vertex_a, 214)
g.add_undirected_edge(vertex_s, vertex_b, 200)
g.add_undirected_edge(vertex_s, vertex_c, 675)
g.add_undirected_edge(vertex_a, vertex_b, 264)
g.add_undirected_edge(vertex_a, vertex_d, 202)
g.add_undirected_edge(vertex_b, vertex_d, 329)
g.add_undirected_edge(vertex_b, vertex_h, 190)
g.add_undirected_edge(vertex_d, vertex_f, 216)
g.add_undirected_edge(vertex_h, vertex_f, 224)
g.add_undirected_edge(vertex_h, vertex_g, 276)
g.add_undirected_edge(vertex_g, vertex_e, 367)
g.add_undirected_edge(vertex_e, vertex_k, 249)
g.add_undirected_edge(vertex_k, vertex_i, 232)
g.add_undirected_edge(vertex_k, vertex_j, 213)
g.add_undirected_edge(vertex_i, vertex_j, 263)
g.add_undirected_edge(vertex_i, vertex_l, 235)
g.add_undirected_edge(vertex_l, vertex_j, 211)
g.add_undirected_edge(vertex_l, vertex_c, 263)

# Run Dijkstra's algorithm first.
dijkstra_shortest_path(g, vertex_d)

# Sort the vertices by the label for convenience; display shortest path for each vertex
# from vertex_a.
for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
    if v.pred_vertex is None and v is not vertex_d:
        print("D to %s: no path exists" % v.label)
    else:
        print("D to %s: %s (total weight: %g)" %
              (v.label, get_shortest_path(vertex_d, v), v.distance))
