# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。 
# 
#  注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
#  
# 
#  示例 2： 
# 
#  输入：a = "a", b = "aa"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：a = "a", b = "a"
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：a = "abc", b = "wxyz"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length <= 10⁴ 
#  1 <= b.length <= 10⁴ 
#  a 和 b 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 字符串匹配 👍 286 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        对于「下界」的分析是容易的：至少将 a 复制长度大于等于 b 的长度，才有可能匹配。
        由于主串是由 a 复制多次而来，并且是从主串中找到子串 b，因此可以明确子串的起始位置，不会超过 a 的长度。
        即长度越过 a 长度的起始匹配位置，必然在此前已经被匹配过了。
        由此，我们可知复制次数「上界」最多为「下界 + 1」。
        子串的起始位置，不会超过 a 的长度。

        因此我们可以对 a 复制 c2 次，得到主串后匹配 b，
        如果匹配成功后的结束位置不超过了 n∗c1，说明复制 c1 即可，返回 c1，超过则返回 c2；匹配不成功则返回 −1。

        :param a:
        :param b:
        :return:
        """

        ans = 0
        sb = ""
        while len(sb) < len(b) and ans +1 > 0:
            ans += 1
            sb+=a
        sb+=a

        idx = sb.find(b)
        if idx == -1:
            return -1
        if idx + len(b) > len(a) * ans :
            return ans +1
        else:
            return ans


# leetcode submit region end(Prohibit modification and deletion)
