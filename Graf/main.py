from Graf.Graph import Graph
from Graf.GraphNode import GraphNode

if __name__ == '__main__':

    g = Graph(directed=True)
    n1 = GraphNode('a')
    n2 = GraphNode('b')
    n3 = GraphNode('c')
    n4 = GraphNode('d')

    g.add_nodes([n1,n2,n3, n4])

    g.add_edges([(n1, n2), (n1, n3), (n2, n3)])

    g.represent_graph()