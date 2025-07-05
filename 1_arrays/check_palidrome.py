def check_palidrome(text):
    left = 0 
    right = len(text) -1 
    while left < right: 
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True 

text = "racecar"
test = check_palidrome(text)
print("test 1: racecar ", test)

text = "rabbit"
test = check_palidrome(text)
print("test 2: rabbit ", test)
