# Finding the sum of natural numbers
def sumSeries(num):
    if num == 1:
        return 1  # BASE CASE
    else:
        return num + sumSeries(num - 1)  # RECURSIVE CASE


print(sumSeries(4))
print(sumSeries(3))
