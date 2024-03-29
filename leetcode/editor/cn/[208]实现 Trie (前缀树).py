# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼
# 写检查。 
# 
#  请你实现 Trie 类： 
# 
#  
#  Trie() 初始化前缀树对象。 
#  void insert(String word) 向前缀树中插入字符串 word 。 
#  boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 
# false 。 
#  boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否
# 则，返回 false 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length, prefix.length <= 2000 
#  word 和 prefix 仅由小写英文字母组成 
#  insert、search 和 startsWith 调用次数 总计 不超过 3 * 10⁴ 次 
#  
# 
#  Related Topics 设计 字典树 哈希表 字符串 👍 1282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Node:
#     def __init__(self):
#         self.children = dict()
#         self.isEnd = False

# class Trie:
#
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self, word: str) -> None:
#         cur = self.root
#         for ch in word:
#             if ch not in cur.children:
#                 cur.children[ch] = Node()
#             cur = cur.children[ch]
#
#         cur.isEnd = True
#
#     def search(self, word: str) -> bool:
#         cur = self.root
#         for ch in word:
#             if ch not in cur.children:
#                 return False
#             cur = cur.children[ch]
#
#         return cur is not None and cur.isEnd
#
#     def startsWith(self, prefix: str) -> bool:
#         cur = self.root
#         for ch in prefix:
#             if ch not in cur.children:
#                 return False
#             cur = cur.children[ch]
#
#         return cur is not None


class Trie:
    class Node:
        def __init__(self):
            self.children = [None for _ in range(26)]
            self.isEnd = False
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if cur.children[ord(ch) - ord('a')] is None:
                cur.children[ord(ch) - ord('a')] = self.Node()
            cur = cur.children[ord(ch) - ord('a')]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if cur.children[ord(ch) - ord('a')] is None:
                return False
            cur = cur.children[ord(ch) - ord('a')]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if cur.children[ord(ch) - ord('a')] is None:
                return False
            cur = cur.children[ord(ch) - ord('a')]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
