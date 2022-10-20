import math


def mergeSort(items):
    print(".......mergeSort() called on:", items)

    # BASE CASE - Zero or one item is naturally sorted.
    if len(items) == 0 or len(items) == 1:
        return items

    # RECURSIVE CASE - Pass the left and right half to the mergeSort():
    # Round down if items doesn't divide in half evenly:
    iMiddle = math.floor(len(items) / 2)
    print("..............Split into: ", items[:iMiddle], "and", items[iMiddle:])

    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])

    # BASE CASE - Returned merged, and sorted data.
    # At this point, left should be sorted and right
    # right should be sorted. We can merge them into a single sorted list.
    sortedResult = []
    iLeft = 0
    iRight = 0
    while len(sortedResult) < len(items):
        # Append the smaller value to the sorteResult.
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1

        # If one of the pointers reached to the end of the list
        # put the rest of the other list into the sortedResult.
        if iLeft == len(left):
            sortedResult.extend(right[iRight:])
            break
        elif iRight == len(right):
            sortedResult.extend(left[iLeft:])
            break

    print("The two halves merge into: ", sortedResult)
    return sortedResult  # Return the sorted version of the items


myList = [2, 9, 8, 5, 3, 4, 7, 6]
myList = mergeSort(myList)
print(myList)
