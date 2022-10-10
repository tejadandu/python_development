def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return True
    else:
        # RECURSIVE CASE
        head = theString[0]
        middle = theString[1:-1]
        tail = theString[-1]
        return tail == head and isPalindrome(middle)


text = "madam"
print(text + " is a palindrome: " + str(isPalindrome(text)))
print(isPalindrome(""))
print(isPalindrome("X"))
