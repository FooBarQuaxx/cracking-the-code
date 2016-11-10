class Node(object):

    def __init__(self, d):
        self.d = d
        self.next = None

    def append(self, d):
        end = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end
        return self

    def _as_list(self):
        l = [self.d]
        n = self.next
        while n is not None:
            l.append(n.d)
            n = n.next
        return l

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self._as_list() == other._as_list()

    def __iter__(self):
        n = self
        yield n
        while n.next is not None:
            n = n.next
            yield n


    @classmethod
    def from_list(cls, l):
        assert len(l) > 0, 'Paramter must have at least one element on it.'
        ll = cls(l[0])
        [ll.append(x) for x in l[1:]]
        return ll


    def __repr__(self):
        return str(self._as_list())
