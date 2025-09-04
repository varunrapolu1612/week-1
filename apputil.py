Exercise - 1
def palindrome(word):
    word = word.lower()
    
    cleaned = ""
    for i in word:
        if i.isalnum():
            cleaned += i
    
    reversed_word = ""
    for j in cleaned:
        reversed_word = j + reversed_word

    if cleaned == reversed_word:
        return "Palindrome"
    else:
        return "Not Palindrome"

Exercise - 2
def parentheses(sequence):
    count = 0
    for i in sequence:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
