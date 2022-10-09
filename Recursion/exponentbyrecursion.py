def exponentByRecursion(a, n):
    if n == 1:
        return a  # BASE CASE
    elif n % 2 == 0:
        # RECURSIVE CASE when n is even
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        # RECURSIVE CASE when n is odd
        result = exponentByRecursion(a, n // 2)
        return result * result * a


print(exponentByRecursion(3, 6))
print(exponentByRecursion(10, 3))
print(exponentByRecursion(17, 10))
