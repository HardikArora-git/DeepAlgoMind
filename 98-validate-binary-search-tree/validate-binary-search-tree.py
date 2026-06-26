# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # check tree root is null or not null
        # if root == None:
        #     return True
        # # left = root
        # # right = root
        # # check the root values left or right are valid acc condition
        # # while root:
        # if (root.left and root.val > root.left.val) and (root.right and root.val < root.right.val):
        # # check(root)
        #     return True
        # else:
        #     return False
        
        # left = self.isValidBSt(root.left,)
        # right = self.isValidBSt(root.right)

        # return root
# print(check(root)
        def valid(root, low=-float("inf"), high=float("inf")):
            if root is None:
                return True

            if not (low < root.val < high):
                return False

            return (valid(root.left, low, root.val) and
                    valid(root.right, root.val, high))

        return valid(root)