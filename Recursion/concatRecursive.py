def concat(string):
    if len(string) == 0 or len(string) == 1:
        # BASE CASE
        return string
    else:
        head = string[0]
        tail = string[1:]
        # RECURSIVE CASE
        return "".join(head) + "".join(concat(tail))


print(concat(["Hello", "World!"]))
