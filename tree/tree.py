class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    nodes: list[int] = [1, 2, 4, -1, -1, 3, -1, 6, -1, -1]
    idx: int = -1
    def __init__(self, nodes: list[int] = []) -> None:
        if len(nodes) > 0:
            self.nodes: list[int] = nodes

    def create(self) -> TreeNode | None:
        self.idx += 1
        if self.idx >= len(self.nodes):
            return None
        if self.nodes[self.idx] == -1:
            return None
        node = TreeNode(self.nodes[self.idx])
        node.left = self.create()
        node.right = self.create()
        return node


tree = BinaryTree()
root: TreeNode = tree.create()
print(f'The root node value is {root.val}')