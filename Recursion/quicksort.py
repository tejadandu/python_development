def quicksort(items, left=None, right=None):
    # By the default `left` and `right` span the list of `items`.
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1  # `right` defaults to the last imdex.

    print("\nquicksort() called on this range:", items[left : right + 1])
    print("...............the full list is: ", items)

    if right <= left:
        # With only zero or one item, `items` are already sorted
        return  # BASE CASE

    # START OF THE PARTITIONING
    i = left  # i start at the left end of the range.
    pivotValue = items[right]  # Select the last value for the pivot.

    print(".............. the pivot is: ", pivotValue)

    # iterate upto , but not including the pivot
    for j in range(left, right):
        # if the value is in the left side of the pivot , swap it so that
        # it's on the left side of the `items`.
        if items[j] <= pivotValue:
            # Swap these two values
            items[i], items[j] = items[j], items[i]
            i += 1
    # Put the pivot on the left side of the `items`
    items[i], items[right] = items[right], items[i]
    # END OF THE PARTITIONING

    print(".....After swaping the range is: ", items[left : right + 1])
    print("Recursively calling quicksort on: ", items[left:i], items[i + 1 : right + 1])

    # Call quicksort() on the two partitions
    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)


# myList = [0, 7, 6, 3, 1, 2, 5, 4]
# quicksort(myList)
# print(myList)
myList1 = [81, 48, 94, 87, 83, 14, 6, 42]
quicksort(myList1)
print(myList1)
