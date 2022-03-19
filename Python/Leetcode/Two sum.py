"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

"""

class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     #n^2
    #     ls = len(nums)
    #     for i in range(ls):
    #         for j in range(i + 1, ls):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # def twoSum(self, nums, target):
    #     # hash 1
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         try:
    #             hash_nums[num].append(index)
    #         except KeyError:
    #             hash_nums[num] = [index]
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             candicate = hash_nums[another]
    #             if another == num:
    #                 if len(candicate) > 1:
    #                     return candicate
    #                 else:
    #                     continue
    #             else:
    #                 return [index, candicate[0]]
    #         except KeyError:
    #             pass

    # def twoSum(self, nums, target):
    #     # hash 2
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             hash_nums[another]
    #             return [hash_nums[another], index]
    #         except KeyError:
    #             hash_nums[num] = index

    def twoSum(self, nums, target):
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
