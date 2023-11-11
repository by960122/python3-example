from typing import List


# 给定一个整数数组 nums和一个整数目标值 target, 请你在该数组中找出 和为目标值 target 的那两个整数, 并返回它们的数组下标. 
# 你可以假设每种输入只会对应一个答案. 但是, 数组中同一个元素在答案里不能重复出现. 
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为 nums[0] + nums[1] == 9, 返回[0, 1]

# 首先,nums[i+1:]是一个切片操作,它会获取nums列表中从i+1位置开始到最后的所有元素. 这样做的目的是在nums[i]之后的元素中寻找第二个加数. 
# 然后,.index(res)会在切片后的列表中查找res(即第二个加数)的索引. 请注意,这个索引是相对于切片后的列表的,也就是说,它是从0开始计数的. 
# 最后,由于我们希望得到的是第二个加数在原始列表nums中的索引,而不是在切片后的列表中的索引,所以需要加上i+1来得到正确的结果. 这是因为切片操作会创建一个新的列表,新列表中元素的索引会从0开始重新计数
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 遍历列表
        for index in range(len(nums)):
            # 计算需要找到的下一个目标数字
            res = target - nums[index]
            # 遍历剩下的元素,查找是否存在该数字
            if res in nums[index + 1:]:
                # 若存在,返回答案. 这里由于是两数之和,可采用.index()方法
                # 获得目标元素在nums[index+1:]这个子数组中的索引后,还需加上i+1才是该元素在nums中的索引
                return [index, nums[index + 1:].index(res) + index + 1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, 9))
