# 设计一个 map ，满足以下几点: 
# 
#  
#  字符串表示键，整数表示值 
#  返回具有前缀等于给定字符串的键的值的总和 
#  
# 
#  实现一个 MapSum 类： 
# 
#  
#  MapSum() 初始化 MapSum 对象 
#  void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 
# key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。 
#  int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# 输出：
# [null, null, 3, null, 5]
# 
# 解释：
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // 返回 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // 返回 5 (apple + app = 3 + 2 = 5)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= key.length, prefix.length <= 50 
#  key 和 prefix 仅由小写英文字母组成 
#  1 <= val <= 1000 
#  最多调用 50 次 insert 和 sum 
#  
# 
#  Related Topics 设计 字典树 哈希表 字符串 👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.val = 0


class MapSum2:
    # 方法一：利用Trie树
    def __init__(self):
        self.map = dict()
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val  # 思考一下，这里为何要用delta保存val？
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val

        node = self.root
        for c in key:
            if node.children[ord(c) - ord('a')] is None:
                node.children[ord(c) - ord('a')] = TrieNode()
            node = node.children[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.children[ord(c) - ord('a')] is None:
                return 0
            node = node.children[ord(c) - ord('a')]
        return node.val


class MapSum4:
    # 方法二：利用哈希表查找对应前缀给定的值
    def __init__(self):
        self.map = {}
        self.prefixmap = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        for i in range(len(key)):
            currprefix = key[0:i + 1]
            if currprefix in self.prefixmap:
                self.prefixmap[currprefix] += delta
            else:
                self.prefixmap[currprefix] = delta

    def sum(self, prefix: str) -> int:
        if prefix in self.prefixmap:
            return self.prefixmap[prefix]
        else:
            return 0


class MapSum3:
    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key in self.map:
            if key.startswith(prefix):
                res += self.map[key]
        return res


class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if node.children[ord(ch) - ord('a')] is None:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if node.children[ord(ch) - ord('a')] is None:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]

        def getSum(node):
            if node is None:
                return 0
            result = node.val
            for child in node.children:
                result += getSum(child)
            return result

        return getSum(node)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# leetcode submit region end(Prohibit modification and deletion)
