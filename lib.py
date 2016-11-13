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

    def __key(self):
            return (self.d)

    def __hash__(self):
        return hash(self.__key())
        pass

    def __str__(self):
        return '->'.join([str(e) for e in self._as_list()])

    def __repr__(self):
        return 'Node(' + ', '.join([str(e) for e in self._as_list()]) + ')'


class Stack(object):

    def __init__(self, elements=None):
        self._data = elements if elements is not None else []
        self._min = min(self._data) if len(self._data) > 0 else None

    @property
    def min(self):
        return self._min

    def _update_min_for_push(self, value):
        if value is None:
            self._min = None
        elif (self._min is None) or \
             (self._min is not None and value < self._min):
            self._min = value

    def _update_min_for_pop(self, value):
        new_min = None
        if value is not None and value == self.min:
            new_min = min(self._data) if len(self._data) > 0 else None
        self._min = new_min

    def push(self, value):
        self._update_min_for_push(value)
        self._data.append(value)

    def pop(self):
        if len(self._data) == 0:
            value = None
        else:
            value = self._data.pop()
        self._update_min_for_pop(value)
        return value

    def __len__(self):
        return len(self._data)

    @property
    def size(self):
        return len(self)


class Queue(object):

    def __init__(self, elements=None):
        self._data = elements if elements is not None else []

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            value = None
        else:
            value, self._data = self._data[0], self._data[1:]
        return value

    def __len__(self):
        return len(self._data)


def test_stack_create():
    obj = Stack()
    assert len(obj) == 0
    obj = Stack([1])
    assert len(obj) == 1


def test_stack_push():
    obj = Stack()
    obj.push(1)
    assert len(obj) == 1


def test_stack_pop():
    obj = Stack([1, 2])

    assert obj.pop() == 2
    assert len(obj) == 1

    assert obj.pop() == 1
    assert len(obj) == 0

    assert obj.pop() is None


def test_stack_min():
    s = Stack()
    assert s.min is None
    s.push(3)
    assert s.min is 3
    s.push(2)
    s.push(1)
    assert s.min is 1
    assert s.pop() is 1
    assert s.min is 2
    s.pop()
    s.pop()
    assert s.min is None


def test_queue_create():
    obj = Queue([1])
    assert len(obj) == 1


def test_queue_enqueue():
    obj = Queue()
    obj.enqueue(1)
    assert len(obj) == 1

    obj.enqueue(2)
    assert len(obj) == 2


def test_queue_dequeue():
    obj = Queue([1, 2, 3])
    assert obj.dequeue() == 1
    assert len(obj) == 2

    assert obj.dequeue() == 2
    assert len(obj) == 1

    assert obj.dequeue() == 3
    assert len(obj) == 0

    assert obj.dequeue() is None
