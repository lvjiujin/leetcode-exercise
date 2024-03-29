# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。 
# 
#  
# 
#  你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#  
# 
#  示例 2: 
# 
#  输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0
# .05556,0.02778] 
# 
#  
# 
#  限制： 
# 
#  1 <= n <= 11 
# 
#  Related Topics 数学 动态规划 概率与统计 👍 496 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def dicesProbability(self, n: int) -> List[float]:
        # dp[i][j] 投掷i个骰子，点数之和为j一共有多少投掷方法？
        dp = [[0] * (6*n + 1) for _ in range(n+1)] # dp[n][6n] n个骰子，点数最多为6n.
        for i in range(1, 7): # 只投掷一次时，点数之和从1到6都只有一种投掷方法。
            dp[1][i] = 1

        for i in range(2, n+1):
            for j in range(i, 6*n + 1):
                for k in range(1, 7):
                    if j - k < i - 1: # 点数之和减去第n次的骰子点数要大于等于骰子数目-1.即要满足每次骰子的点数最低为1的要求。
                        break
                    dp[i][j] += dp[i-1][j-k]

        res = [0.0] * (5 * n + 1)
        for i in range(n, 6*n+1):
            res[i-n] = dp[n][i] / (6 ** n)

        return res

    def dicesProbability2(self, n: int) -> List[float]:
        # 节省内存的代码不容易看懂。
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp


# leetcode submit region end(Prohibit modification and deletion)
