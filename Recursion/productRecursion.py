def product(numbers):
    if len(numbers) == 0:
        # BASE CASE
        return 1
    else:
        head = numbers[0]
        tail = numbers[1:]
        # RECURSIVE CASE
        return head * product(tail)


print(product([3, 2, 4, 5, 6]))
