'''To perform an inorder traversal of a binary tree, we need to visit the nodes in the following order:

Visit the left subtree.
Visit the current node.
Visit the right subtree.
We can perform this traversal recursively. At each node, we first visit the left subtree by recursively calling the function on the left child. Then, we visit the current node and append its value to the result. Finally, we visit the right subtree by recursively calling the function on the right child.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        def inorderTraversalHelper(node, result):
            if node is None:
                return

            inorderTraversalHelper(node.left, result)
            result.append(node.val)
            inorderTraversalHelper(node.right, result)

        inorderTraversalHelper(root, result)
        return result
    
'''
I start with an empty result list and pass it as a parameter to a helper function, inorderTraversalHelper, along with the root node.
The inorderTraversalHelper function first checks if the current node is None. If it is, i simply return without doing anything.
Otherwise, i first visit the left subtree by recursively calling inorderTraversalHelper on the left child of the current node. This will append all the values in the left subtree to the result list in the correct order.
I then append the value of the current node to the result list.
Finally, i visit the right subtree by recursively calling inorderTraversalHelper on the right child of the current node. This will append all the values in the right subtree to the result list in the correct order.
At the end, i simply return the result list, which will contain the inorder traversal of the binary tree.
'''
