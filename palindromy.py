def is_the_word_palindrome(word):

    if word == word[::-1]:
        return True
    else:
        return False
    
"""Description of the definition

    Args:
        word: You put any word you like to check if its palindrome

    if function word == word[::1] checks if word written backwards matches the original word (palindrome)
      
    Returns:
        Boolean: Returns if the word is Palindrome or not (True or False)
"""
   
print(is_the_word_palindrome("wojtek"))
print(is_the_word_palindrome("anna"))
