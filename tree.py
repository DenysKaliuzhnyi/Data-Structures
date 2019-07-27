class Node:
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

    def __str__(self):
        return str(self.data)

    def __del__(self):
        if self.left is not None:
            del self._left
        if self.right is not None:
            del self._right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


class Tree:
    def __init__(self):
        self._root = None
        self._high = 1

    def __str__(self):
        def _row(node):
            nonlocal res
            res = f"{res}{str(node.data)}, "
            if node.left is not None:
                _row(node.left)
            if node.right is not None:
                _row(node.right)

        if self._root is None:
            return "{}"
        res = "{"
        _row(self._root)
        res = res[:-2] + '}'
        return res

    def add(self, value):
        def _add(value, node):
            nonlocal deep
            if value < node.data:
                if node.left is None:
                    node.left = Node(value)
                else:
                    _add(value, node.left)
            elif value > node.data:
                if node.right is None:
                    node.right = Node(value)
                else:
                    _add(value, node.right)
            else:
                return
            deep += 1

        deep = 1
        if self._root is None:
            self._root = Node(value)
        else:
            _add(value, self._root)
            if deep > self._high:
                self._high = deep

    def find(self, value):
        def _find(node, value):
            if value == node.value:
                return node
            elif value < node.value and node.left is not None:
                _find(node.left, value)
            elif value > node.value and node.right is not None:
                _find(node.right, value)

        if self._root is not None:
            return _find(self._root, value)

    def clear(self):
        del self._root
        self._root = None
        self._high = 1

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(2)
tree.add(4)
tree.add(9)
tree.add(8)
tree.add(1)
tree.add(6)
tree.add(2)
tree.add(7)
tree.add(11)
tree.add(10)

tree.clear()

print(tree)