# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!
# =b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。 
# 
#  只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
#  
# 
#  示例 2： 
# 
#  输入：["b==a","a==b"]
# 输出：true
# 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
#  
# 
#  示例 3： 
# 
#  输入：["a==b","b==c","a==c"]
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：["a==b","b!=c","c==a"]
# 输出：false
#  
# 
#  示例 5： 
# 
#  输入：["c==c","b==d","x!=z"]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 500 
#  equations[i].length == 4 
#  equations[i][0] 和 equations[i][3] 是小写字母 
#  equations[i][1] 要么是 '='，要么是 '!' 
#  equations[i][2] 是 '=' 
#  
# 
#  Related Topics 并查集 图 数组 字符串 👍 257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    class UnionFind:
        def __init__(self):
            # 初始化,parent[i] =i 祖先的祖先是自己。
            self.parent = [i for i in range(26)]

        def find(self, index):
            if self.parent[index] == index:
                return index
            # 递归，不断向上查找其祖先。
            self.parent[index] = self.find(self.parent[index])

            return self.parent[index]

        def union(self, index1, index2):
            root1 = self.find(index1)
            root2 = self.find(index2)
            # root1的祖先指向root2，root2成为公共祖先。
            self.parent[root1] = root2

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for t in equations:
            # 先循环找出所有的联通分量，即union。
            if t[1] == '=':
                x = ord(t[0]) - ord('a')
                y = ord(t[3]) - ord('a')
                uf.union(x, y)
        # 再循环处理非联通的分量。
        for t in equations:
            if t[1] == '!':
                x = ord(t[0]) - ord('a')
                y = ord(t[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
