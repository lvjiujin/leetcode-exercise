# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 342 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 反向中序遍历.

        cur = root
        stack = []
        i = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            node = stack.pop()
            i += 1
            if i == k:
                return node.val

            if node.left:
                cur = node.left

        return 0


# leetcode submit region end(Prohibit modification and deletion)
