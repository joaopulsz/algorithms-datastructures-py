class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])

    def add_vertex(self, value):
        if value not in self.adj_list.keys():
            self.adj_list[value] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True


graph = Graph()

graph.add_vertex("J")
graph.add_vertex("O")

print(graph.add_edge("J", "A"))
print(graph.add_edge("O", "J"))

graph.print_graph()
