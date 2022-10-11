import sys

img = [
    list("..########################..........."),
    list("..#......................#...#####..."),
    list("..#..........########....#####...#..."),
    list("..#..........#......#............#..."),
    list("..#..........########.........####..."),
    list("..######......................#......"),
    list(".......#..#####.....###########......"),
    list(".......####...#######................"),
]
HEIGHT = len(img)
WIDTH = len(img[0])


def floodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        # BASE CASE
        return
    image[y][x] = newChar
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x - 1, y, newChar, oldChar)
    return


def printImage(image):
    for y in range(HEIGHT):
        # Print each row
        for x in range(WIDTH):
            # Print each column
            sys.stdout.write(image[y][x])
        sys.stdout.write("\n")
    sys.stdout.write("\n")


printImage(img)
floodFill(img, 3, 3, "o")
printImage(img)
