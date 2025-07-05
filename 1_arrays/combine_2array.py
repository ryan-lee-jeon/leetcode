"""
Given two sorted integer arrays arr1 and arr2, 
return a new array that combines both of them and is also sorted.
"""

def combine_arrays(arr1, arr2):
    i = j = 0
    solution = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            solution.append(arr1[i])
            i +=1
        else:
            solution.append(arr2[j])
            j +=1
    
    while i < len(arr1):
        solution.append(arr1[i])
        i+=1

    while j < len(arr2):
        solution.append(arr2[j])
        j+=1
    return solution

arr1 = [3, 6, 21, 23, 25] 
arr2 = [4, 5, 20, 22, 24] 

test = combine_arrays(arr1, arr2)
print(test)

