class Solution16:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        best = 10 ** 7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for first in range(length):
            # 保证和上一次枚举的元素不相等
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 使用双指针枚举 b 和 c
            second, third = first + 1, length - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                # 如果和为 target 直接返回答案
                if sum == target:
                    return target
                update(sum)
                if sum > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = third - 1
                    # 移动到下一个不相等的元素
                    while second < k0 and nums[k0] == nums[third]:
                        k0 -= 1
                    third = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = second + 1
                    # 移动到下一个不相等的元素
                    while j0 < third and nums[j0] == nums[second]:
                        j0 += 1
                    second = j0

        return best
