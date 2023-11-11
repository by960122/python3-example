# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 
# 算法的时间复杂度应该为 O(log (m+n)) .
# 
# 示例 1：
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ,中位数 2
# 示例 2：
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ,中位数 (2 + 3) / 2 = 2.5
class Solution4:
    # >> 1 相当于 / 2
    def findMedianSortedArrays(self, nums1, nums2):
        nums3, l = sorted(nums1 + nums2), len(nums1) + len(nums2)
        return nums3[l >> 1] if l & 1 else (nums3[l >> 1 - 1] + nums3[l >> 1]) / 2.0
