def sum(numbers):
    if len(numbers) == 0:  # BASE CASE
        return 0
    else:  # RECURSIVE CALL
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)


print(sum([5, 4, 3, 8]))
nums = [5, 2, 4, 8]
print("sum of", nums, "is", sum(nums))
