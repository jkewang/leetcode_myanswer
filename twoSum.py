import numpy as np


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a = np.array(nums)
        result = np.array([1, 2])
        for i in range(len(a)):
            interest_num = target - a[i]
            index = np.argwhere(a == interest_num)
            if len(index) != 0:
                result[0] = i
                result[1] = index[0][0]
                break

        return result

a = Solution()
result = a.twoSum()
print(result)

