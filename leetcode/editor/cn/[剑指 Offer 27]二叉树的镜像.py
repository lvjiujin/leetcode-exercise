# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。 
# 
#  例如输入： 
# 
#  4 / \ 2 7 / \ / \ 1 3 6 9 镜像输出： 
# 
#  4 / \ 7 2 / \ / \ 9 6 3 1 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 1000 
# 
#  注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 317 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        import collections
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        # 递归翻转二叉树的左右子树
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root



# leetcode submit region end(Prohibit modification and deletion)
