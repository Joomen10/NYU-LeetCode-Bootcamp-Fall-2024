# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None

        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)

        # root.left = right
        # root.right = left
        # return root

        if not root:
            return None
        
        queue = collections.deque([root])
        while queue:
            current = queue.popleft()
            current.right, current.left = current.left, current.right

            if current.right:
                queue.append(current.right)

            if current.left:
                queue.append(current.left)

        return root





        

        