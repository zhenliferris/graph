class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []


# Program to create and populate a Graph object.
g = Graph()
vertex_a = Vertex("New York")
vertex_b = Vertex("Tokyo")
vertex_c = Vertex("London")

g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
