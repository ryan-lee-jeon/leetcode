'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0 
    while left < len(nums):
        nums[left] = nums[left] * nums[left]
        left += 1
    nums.sort()
    return nums

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))