def is_the_word_palindrome(sentence):
    word = ""
    for char in sentence:
        if char.isalnum():
            word += char.lower()
    return word == word[::-1]

"""Description of the definition

 Code checks if the words you type are palindromes (written from the back are same as written from the start)
 Method char.isalnum() is responsible for letters and numbers and it ignoress the special signs like @ # etc
 Method char.lower() is responsible for capital letters and it makes them all lower case. This way it doesn't matter if user types sentence with capital letters or not.
""" 
print(is_the_word_palindrome("wojtek"))
print(is_the_word_palindrome("Anna"))
print(is_the_word_palindrome("Mariusz@.13423"))
print(is_the_word_palindrome("...12Kajak21#@."))
