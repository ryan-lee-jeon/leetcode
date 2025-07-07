# Example 2: 
# You are given a binary string s (a string containing only "0" and "1"). 
# You may choose up to one "0" and flip it to a "1". 

# What is the length of the longest substring achievable that contains only "1"?

s = "1101100111"
test_answer = 5


def zeroes_ones(string):
    right = 0
    left = 0 
    current = 0
    answer = 0

    # don't forget range(len(s))
    for right in range(len(string)):
        if string[right] == "0":
            current += 1
        while current > 1:
            if string[left] == "0":
                current -=1 
            left +=1
        answer = max(answer, right - left +1)
    return answer

test = zeroes_ones(s)
print(test)