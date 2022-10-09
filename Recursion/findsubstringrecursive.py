def findSubstringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1  # BASE CASE
    if haystack[i : i + len(needle)] == needle:
        return i  # RECURSIVE CASE
    else:
        return findSubstringRecursive(needle, haystack, i + 1)


print(findSubstringRecursive("cat", "my cat zophie"))
