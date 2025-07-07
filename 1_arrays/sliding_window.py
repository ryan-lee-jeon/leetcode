'''Example 1: 
Given an array of positive integers nums and an integer k, 
find the length of the longest subarray whose sum is less than or equal to k. 
'''

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] 
k = 8

def length_subarray(nums, k):
    current = 0 
    maximum = 0
    left = 0
    right = 0 

    for right in range(len(nums)):
        current += nums[right]

# don't need a right +=1 because the for loop is already doing that
        while current > k:
            current -= nums[left]
            left +=1
        
        maximum = max(maximum, right - left + 1) # remember the right - left + 1
    return maximum 
    
test = length_subarray(nums, k)
print(test)

