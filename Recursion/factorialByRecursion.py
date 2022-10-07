def factorial(number):
    if number == 1 or number == 0:
        #BASE CASE
        return 1
    else:
        #RECURSIVE CASE
        return number * factorial(number - 1)

print('Factorial of given number: ')
print(factorial(4))
