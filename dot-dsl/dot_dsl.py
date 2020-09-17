# TODO: Running tests individually it pass, when running all at once it fails with Lists Differ (pytest 6 / python 3.8)

NODE, EDGE, ATTR = range(3)


class Component(object):
    _schema = NotImplemented

    @classmethod
    def validate(cls, args):
        return all(isinstance(a, t) for a, t in zip(args, cls._schema))


class Node(Component):
    _schema = (str, (dict, set))

    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(Component):
    _schema = (str, str, dict)

    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src
                and self.dst == other.dst
                and self.attrs == other.attrs)


class Attr(Component):
    _schema = (str, str)

    def __init__(self, key, value):
        self.kv = (key, value)


class Graph:
    edges = []
    nodes = []
    _attrs = []

    _graph = {
        NODE: (Node, nodes),
        EDGE: (Edge, edges),
        ATTR: (Attr, _attrs),
    }

    def __init__(self, data=[]):
        if not self._valid_data(data):
            raise TypeError('Invalid DSL')

        for tup in data:
            entity_type, args = tup[0], tup[1:]
            try:
                entity, storage = self._graph[entity_type]
            except KeyError:
                raise ValueError('Invalid graph entity `{}`'.format(entity_type))

            if not entity.validate(args):
                raise ValueError('Invalid {}'.format(entity.__name__))

            storage.append(entity(*args))

    @property
    def attrs(self):
        return dict(a.kv for a in self._attrs)

    def _valid_data(self, data):
        return all(isinstance(x, tuple) and len(x) > 0 for x in data)
