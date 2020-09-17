from typing import List
import sys

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

    def __init__(self, data: List = []):
        try:
            for d in data:
                if d[0] == NODE:
                    self.nodes.append(Node(d[1], d[2]))
                elif d[0] == EDGE:
                    self.edges.append(Edge(d[1], d[2], d[3]))
                elif d[0] == ATTR:
                    self.attrs.update({d[1]: d[2]})
                else:
                    raise ValueError('Invalid entity')
        except IndexError:
            raise ValueError('Invalid entity attributes')
