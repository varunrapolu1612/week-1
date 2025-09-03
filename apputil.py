# Exercise-1:
def palindrome(word):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False
    return True

# Exercise -2:
'''
def Brackets(x):
    count = 0
    for char in x:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False #closing > opening
    return count == 0  #Done!
'''
