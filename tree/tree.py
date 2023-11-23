from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    nodes: list[int] = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    idx: int = -1
    def __init__(self, nodes: list[int] = []) -> None:
        if len(nodes) > 0:
            self.nodes: list[int] = nodes

    def create(self) -> TreeNode:
        def build():
            self.idx += 1
            if self.idx >= len(self.nodes):
                return None
            if self.nodes[self.idx] == -1:
                return None
            node = TreeNode(self.nodes[self.idx])
            node.left = build()
            node.right = build()
            return node
        root = build()
        return root if root else TreeNode()


    """
    Preorder traversal
    Root -> Left -> Right
    """
    def preorder(self, root: Optional[TreeNode], values: list[int]) -> list[int]:
        def pre(root):
            if not root:
                return None
            values.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return values


    """
    Inorder traversal
    Root -> Left -> Right
    """
    def inorder(self, root: Optional[TreeNode], values: list[int]) -> list[int]:
        def pre(root):
            if not root:
                return None
            pre(root.left)
            values.append(root.val)
            pre(root.right)

        pre(root)
        return values


    """
    Postorder traversal
    Root -> Left -> Right
    """
    def postorder(self, root: Optional[TreeNode], values: list[int]) -> list[int]:
        def pre(root):
            if not root:
                return None
            pre(root.left)
            pre(root.right)
            values.append(root.val)

        pre(root)
        return values
    

    """
    Level order traversal
    We will use QUEUE to run level by level
    """
    def levelorder(self, root: Optional[TreeNode], values: list[int]) -> None:
        if not root:
            return
        queue = [root, -1]
        while len(queue) > 0:
            node = queue.pop(0)
            if node == -1:
                print("")
                if len(queue) > 0:
                    queue.append(-1)
            else:
                print(node.val, end=", ")
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
    
    """
    Counting nodes
    Left + Right + 1
    """
    def count(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.count(root.left) + self.count(root.right) + 1
            
    
    """
    Sum of nodes
    Left.val + Right.val + root.val
    """
    def sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.sum(root.left) + self.sum(root.right) + root.val
            
    
    """
    Height of tree
    Left height + Right height + 1
    """
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    """
    Diameter of tree
    diameter = left height + right height + 1
    max diameter = max of left, right, and current diamter
    """
    def diameter(self, root: Optional[TreeNode]) -> int:
        class TreeInfo:
            def __init__(self, ht, dm) -> None:
                self.ht: int = ht
                self.dm: int = dm
        def dm(root) -> TreeInfo:
            if not root:
                return TreeInfo(0, 0) # [height, diameter]
            dm1 = dm(root.left)
            dm2 = dm(root.right)
            height = max(dm1.ht, dm2.ht) + 1
            diameter = dm1.ht + dm2.ht + 1
            dm3 = max(dm1.dm, dm2.dm, diameter)
            return TreeInfo(height, dm3)
        return dm(root).dm


    """
    Diameter of tree
    diameter = left height + right height + 1
    max diameter = max of left, right, and current diamter
    """
    def match(self, root, tree) -> bool:
        if not root and not tree:
            return True
        if not root or not tree:
            return False
        if(root.val == tree.val):
            return self.match(root.left, tree.left) and self.match(root.right, tree.right)
        return False
    
    def match_subtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub:
            return True
        if not root:
            return False
        if root.val == sub.val:
            if self.match(root, sub):
                return True
        return self.match_subtree(root.left, sub) or self.match_subtree(root.right, sub)



    def kth_sum(self, root: Optional[TreeNode], k: int) -> int:
        l = 1
        count = 0
        queue = [root, -1]
        while len(queue) > 0:
            node = queue.pop(0)
            if node == -1:
                l += 1
                if len(queue) > 0:
                    queue.append(-1)
            else:
                if l == k:
                    count += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if l > k:
                return count
        return count


# =====================================
"""
Call all the methods and class which created
"""
tree: BinaryTree = BinaryTree()
root: TreeNode = tree.create()
print(f'The root node value is {root.val}')

preorderList: list[int] = tree.preorder(root, [])
print("Preorder traversal: ", end="")
for x in preorderList:
    print(x, end=", ")

inorderList = tree.inorder(root, [])
print("\nInorder traversal: ", end="")
for x in inorderList:
    print(x, end=", ")


postorderList = tree.postorder(root, [])
print("\nPostOrder traversal: ", end="")
for x in postorderList:
    print(x, end=", ")


print("\nLevelOrder traversal:")
tree.levelorder(root, [])

print(f"\nCount total number of node is: {tree.count(root)}")

print(f"\nCount total value of nodes is: {tree.sum(root)}")

print(f"\nCount the height of nodes is: {tree.height(root)}")

print(f"\nMaximum diameter of nodes is: {tree.diameter(root)}")

print(f"\nMatch subtree of a tree is: {tree.match_subtree(root, root)}")

print(f"\nK th level nodes sum is: {tree.kth_sum(root, 1)}")


