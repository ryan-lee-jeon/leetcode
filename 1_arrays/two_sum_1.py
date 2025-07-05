"""Example 2: 
Given a sorted array of unique integers and a target integer, 
return true if there exists a pair of numbers that sum to target, false otherwise. 
This problem is similar to Two Sum. (In Two Sum, the input is not sorted)."""

def two_sum(array, k):
    left = 0 
    right = len(array)-1


    
    while left < right: 
        current = array[left] + array[right]
        if current == k: 
            return True
        else:
            if current > k: 
                right -= 1
            else: 
                left +=1
    return False 

nums = [3, 6, 21, 23, 25]  
target = 27

test = two_sum(nums, target)
print(test)