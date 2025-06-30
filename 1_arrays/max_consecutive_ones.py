

def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    left = curr = ans = 0 
    for r in range(len(nums)):
        if nums[r] == 0:
            curr += 1
        while curr > k: 
            if nums[left] ==0:
                curr -= 1
            left +=1
        ans = max(ans, r - left +1)
    return ans 

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

answer = longestOnes(nums, k)
print(answer)
