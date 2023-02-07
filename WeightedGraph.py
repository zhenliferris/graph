class Vertex:

    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


g = Graph()
vertex_a = Vertex("Tokyo")
vertex_b = Vertex("New York")
vertex_c = Vertex("London")
vertex_d = Vertex("Sydney")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)

g.add_undirected_edge(vertex_a, vertex_b, 6743)
g.add_undirected_edge(vertex_a, vertex_c, 5941)
g.add_undirected_edge(vertex_a, vertex_d, 4863)
g.add_undirected_edge(vertex_b, vertex_c, 3425)
g.add_undirected_edge(vertex_b, vertex_d, 9868)
g.add_undirected_edge(vertex_c, vertex_d, 10562)