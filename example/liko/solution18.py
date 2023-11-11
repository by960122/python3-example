class Solution18:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for first in range(length - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
                break
            if nums[first] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for second in range(first + 1, length - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                    break
                if nums[first] + nums[second] + nums[length - 2] + nums[length - 1] < target:
                    continue
                third, four = second + 1, length - 1
                while third < four:
                    total = nums[first] + nums[second] + nums[third] + nums[four]
                    if total == target:
                        quadruplets.append([nums[first], nums[second], nums[third], nums[four]])
                        while third < four and nums[third] == nums[third + 1]:
                            third += 1
                        third += 1
                        while third < four and nums[four] == nums[four - 1]:
                            four -= 1
                        four -= 1
                    elif total < target:
                        third += 1
                    else:
                        four -= 1

        return quadruplets
