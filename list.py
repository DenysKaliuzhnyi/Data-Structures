class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class List:
    def __init__(self):
        self._head = None
        self._length = 0

    def __getitem__(self, key):
        if key >= self.length:
            raise IndexError
        current = self._head
        for _ in range(key):
            current = current.next
        return current

    def __iter__(self):
        self._runner = self._head
        return self

    def __next__(self):
        if self._runner is None:
            raise StopIteration
        tmp = self._runner
        self._runner = self._runner.next
        return tmp

    def __contains__(self, item):
        return self.search(item)

    def __str__(self):
        current = self._head
        res = "["
        if current:
            res = f"{res}{str(current)}"
            current = current.next
        while current is not None:
            res = f"{res}, {str(current)}"
            current = current.next
        res = f"{res}]"
        return res

    def __del__(self):
        self.clear()

    @property
    def length(self):
        return self._length

    def add(self, value):
        temp = Node(value)
        temp.next = self._head
        self._head = temp
        self._length += 1

    def remove(self, value):
        current = self._head
        prev = None
        found = False
        while not found and current is not None:
            if current.data == value:
                found = True
            else:
                prev = current
                current = current.next
        if current is None:
            raise KeyError
        if prev is None:
            self._head = current.next
        else:
            prev.next = current.next
        del current
        self._length -= 1

    def search(self, value):
        current = self._head
        found = False
        while not found and current is not None:
            if current.data == value:
                found = True
            else:
                current = current.next
        return found

    def pop(self):
        tmp = self._head.next
        del self._head
        self._head = tmp
        self._length -= 1

    def clear(self):
        while self._head is not None:
            self.pop()


l = List()
l.add("a")
l.add("b")
print(l)
print("a" in l)
l.clear()
print(l)
l.add("aa")
print(l)