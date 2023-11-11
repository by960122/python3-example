# 盛最多水的容器 输入：[1,8,6,2,5,4,8,3,7] 输出：49 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7].在此情况下,容器能够容纳水（表示为蓝色部分）的最大值为 49.
# 每轮向内移动短板,所有消去的状态都 不会导致面积最大值丢失
from typing import List


class Solution11:
    def maxArea(self, height: List[int]) -> int:
        startIndex, endIndex, result = 0, len(height) - 1, 0
        while startIndex < endIndex:
            if height[startIndex] < height[endIndex]:
                result = max(result, height[startIndex] * (endIndex - startIndex))
                startIndex += 1
            else:
                result = max(result, height[endIndex] * (endIndex - startIndex))
                endIndex -= 1
        return result


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution11.maxArea(height))
