'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


'''



def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    current_sum = sum(nums[:k])
    ans_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        ans_sum = max(ans_sum, current_sum)
    return ans_sum/float(k) 
    
        
        
nums = [1,12,-5,-6,50,3]
k = 4

solution = findMaxAverage(nums, k)
print(solution)
