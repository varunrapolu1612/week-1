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
