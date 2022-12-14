# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10â´ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting ð 6777 ð 238


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # æ¹æ³ä¸ï¼æ²¡ææå·§çç¬¨åæ³
        # if not s or not t or len(s) != len(t):
        #     return False
        # d = dict()
        # for x in s:
        #     if x in d:
        #         d[x] +=1
        #     else:
        #         d[x] = 1
        # for y in t:
        #     if y not in d:
        #         return False
        #     else:
        #         d[y] -=1
        # for i in d.values():
        #     if i != 0:
        #         return False
        #
        # return True
    # æ¹æ³äº: ä¸å®è¦æ³å°æåºãä¸å®è¦æ³å°æåºã
    #     if not s or not t or len(s) != len(t):
    #         return False
    #     s = sorted(s)
    #     t = sorted(t)
    #     if s == t:
    #         return True
    #     else:
    #         return False
    # æ¹æ³ä¸ï¼Counter
        from collections import Counter
        return Counter(s) == Counter(t)





        
# leetcode submit region end(Prohibit modification and deletion)
