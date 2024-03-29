# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也
# 视作摆动序列。 
# 
#  
#  例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。 
#  相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一
# 个差值为零。 
#  
# 
#  子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。 
# 
#  给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,7,4,9,2,5]
# 输出：6
# 解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,17,5,10,13,15,10,5,16,8]
# 输出：7
# 解释：这个序列包含几个长度为 7 摆动序列。
# 其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,3,4,5,6,7,8,9]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度完成此题? 
# 
#  Related Topics 贪心 数组 动态规划 👍 796 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        preDiff = nums[1] - nums[0]
        count = 2 if preDiff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and preDiff <=0) or \
                    (diff < 0 and preDiff >= 0):
                count += 1
                preDiff = diff
        return count


    def wiggleMaxLength4(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)

    def wiggleMaxLength3(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = [0] * n, [0] * n
        up[0] = down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] +1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] +1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]

        return max(down[n-1], up[n-1])


    def wiggleMaxLength2(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = [0] * n, [0] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] +1)

        return 1 + max(up[n-1], down[n-1])

# leetcode submit region end(Prohibit modification and deletion)
