

s = ["h","e","l","l","o"]

def reverse_string(s):

    left = 0
    right = len(s)-1

    while left < right: 
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1

reverse_string(s)
print(s)