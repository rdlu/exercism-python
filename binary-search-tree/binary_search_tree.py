from typing import Any, Generator

class TreeNode:
    def __init__(self, data, left:'TreeNode'=None, right:'TreeNode'=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def insert(self, new_data) -> None:
        if new_data <= self.data:
            if self.left is None:
                self.left = TreeNode(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right is None:
                self.right = TreeNode(new_data)
            else:
                self.right.insert(new_data)


class BinarySearchTree:
    def __init__(self, tree_data: list[Any]) -> None:
        head, tail = tree_data[0], tree_data[1:]
        self.root = TreeNode(head)
        for x in tail:
            self.root.insert(x)

    def data(self):
        return self.root

    def sorted_data(self):
        return list(self.root)

    def __iter__(self):
        return iter((node.data for node in self.sorted(self.root)))

    @classmethod
    def sorted(_cls, node: 'TreeNode') -> Generator:
        if node is not None:
            yield from sorted(node.left)
            yield node.data
            yield from sorted(node.right)