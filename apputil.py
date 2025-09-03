def palindrome(word):
    word = word.lower()
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False
    return True
    
