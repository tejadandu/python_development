def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return theString
    else:
        # RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head


print(rev("ajet"))
print(rev(""))
print(rev("Hello, World!"))
print(rev("X"))
