
def is_the_word_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
print(is_the_word_palindrome("wojtek"))
