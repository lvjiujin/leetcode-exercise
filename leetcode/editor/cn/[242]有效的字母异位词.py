# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  Related Topics 哈希表 字符串 排序 👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
        # 解法一：
        # if not s or not t or len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False
        # 解法二:
        # if not s or not t or len(s) != len(t):
        #     return False
        # char_dict = dict()
        # for c in s:
        #     if c in char_dict:
        #         char_dict[c] +=1
        #     else:
        #         char_dict[c] = 1
        # for c in t:
        #     if c not in char_dict:
        #         return False
        #     else:
        #         char_dict[c]-=1
        #
        # for value in char_dict.values():
        #     if value != 0:
        #         return False
        #
        # return True



# leetcode submit region end(Prohibit modification and deletion)
