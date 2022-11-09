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
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys() or vertex1 not in self.adj_list[vertex2] or vertex2 not in self.adj_list[vertex1]:
            return False
        self.adj_list[vertex1].remove(vertex2)
        self.adj_list[vertex2].remove(vertex1)
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False
        for edge in self.adj_list[vertex]:
            self.adj_list[edge].remove(vertex)
        self.adj_list.pop(vertex)
        return True


graph = Graph()

graph.add_vertex("J")
graph.add_vertex("O")
graph.add_vertex("A")
graph.add_vertex("P")

graph.add_edge("O", "J")
graph.add_edge("O", "A")
graph.add_edge("A", "J")

graph.remove_vertex("A")

graph.print_graph()
