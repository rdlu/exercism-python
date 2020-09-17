NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src
                and self.dst == other.dst
                and self.attrs == other.attrs)


class Graph:
    edges = []
    nodes = []
    attrs = {}

    def __init__(self, data=[]):
        if not isinstance(data, list):
            raise TypeError('data must be a list')

        for tup in data:
            if len(tup) != 3 and len(tup) != 4:
                raise TypeError('input is wrong')

            if tup[0] == ATTR:
                self.attrs.update(create_attr(tup[1:]))
            elif tup[0] == NODE:
                self.nodes.append(create_node(tup[1:]))
            elif tup[0] == EDGE:
                self.edges.append(create_edge(tup[1:]))
            else:
                raise ValueError('unknown item')


def create_attr(inputs):
    if not all(isinstance(x, str) for x in inputs):
        raise ValueError('inputs are wrong')
    return {inputs[0]: inputs[1]}


def create_node(inputs):
    if not isinstance(inputs[0], str) or not isinstance(inputs[1], dict):
        raise ValueError('inputs are wrong')
    return Node(inputs[0], inputs[1])


def create_edge(inputs):
    if not (isinstance(inputs[0], str) and isinstance(inputs[1], str)) or not isinstance(inputs[2], dict):
        raise ValueError('inputs are wrong')
    return Edge(inputs[0], inputs[1], inputs[2])
