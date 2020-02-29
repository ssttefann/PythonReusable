
from Graph import Graph
from GraphNode import GraphNode

if __name__ == '__main__':

    g = Graph(directed=True)
    n1 = GraphNode('a')
    n2 = GraphNode('b')
    n3 = GraphNode('c')

    g.add_nodes([n1,n2,n3])

    g.add_edges([(n1, n2), (n1, n3), (n2, n3)])

    g.represent_graph()