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


graph = Graph()

graph.add_vertex("J")
graph.add_vertex("O")

graph.print_graph()
