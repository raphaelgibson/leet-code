from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth First Search
    def invertTree(self, root: TreeNode | None = None) -> TreeNode | None:
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # Breadth First Search
    def invertTreeBFS(self, root: TreeNode | None = None) -> TreeNode | None:
        if not root:
            return root

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root
