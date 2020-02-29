from Graphs.DataStructure.GraphEdge import GraphEdge


class GraphNode:

    def __init__(self, value):
        self.value = value
        self.edges = dict()

    def edge_exists(self, other_node):
        if other_node.value in self.edges:
            return True

        return False

    def add_edge(self, other_node, directed=False):
        if self.edge_exists(other_node):
            return False

        self.edges[other_node.value] = GraphEdge(self, other_node, directed)
        return True

    def write_edges(self):
        print("Node {} :".format(self.value))

        for idx, edge in enumerate(self.edges.values()):
            print('\tEdge {}: value: {}'.format(idx+1, edge.end.value))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, GraphNode):
            return False

        return self.value == o.value

