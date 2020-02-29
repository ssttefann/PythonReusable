from GraphEdge import GraphEdge


class Graph:

    def __init__(self, directed=False):
        self.nodes = dict()
        self.directed = directed

    def add_node(self, node):
        if node.value in self.nodes:
            raise KeyError

        self.nodes[node.value] = node

    def add_nodes(self, nodes):
        [self.add_node(x) for x in nodes]

    def add_edge(self, first_node, second_node):
        first_node.add_edge(second_node, self.directed)

        if not self.directed:
            second_node.add_edge(first_node, self.directed)

    def add_edges(self, tuple_list):
        [self.add_edge(elem[0], elem[1]) for elem in tuple_list]

    def represent_graph(self):
        for node in self.nodes.values():
            node.write_edges()






