def numberOfBinaryTreeTopologies(n):
    if n == 0:
        # BASE CASE
        return 1
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        # RECURSIVE CASE (For left subtree)
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        # RECURSIVE CASE (For right subtree)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees


print(numberOfBinaryTreeTopologies(3))
print(numberOfBinaryTreeTopologies(5))
