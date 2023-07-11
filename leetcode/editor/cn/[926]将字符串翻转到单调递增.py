# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。 
# 
#  给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。 
# 
#  返回使 s 单调递增的最小翻转次数。 
# 
#  
#
#  示例 1： 
# 
#  
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 为 '0' 或 '1' 
#  
# 
#  Related Topics 字符串 动态规划 👍 289 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [[0, 0] for _ in range(2)]

        dp[0][0] = 0 if s[0] == '0' else 1
        dp[1][0] = 0 if s[0] == '1' else 1
        for i in range(1, len(s)):
            prev1 = dp[0][(i - 1) % 2]
            prev2 = dp[1][(i - 1) % 2]
            dp[0][i % 2] = prev1 if s[i] == '0' else prev1 + 1
            dp[1][i % 2] = min(prev1, prev2) + 1 if s[i] == '0' else min(prev1, prev2)
        last = (len(s) - 1) % 2
        
        return min(dp[0][last], dp[1][last])
# leetcode submit region end(Prohibit modification and deletion)
