class GraphEdge:

    def __init__(self, start, end, directed=False):
        self.start = start
        self.end = end
        self.directed = directed

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, GraphEdge):
            return False

        if self.directed:
            return self.start == o.start and self.end == o.end

        else:
            return (self.start == o.start and self.end == o.end) or \
                   (self.start == o.end and self.end == o.start)

