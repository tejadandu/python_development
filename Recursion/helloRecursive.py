print("code in function:")


def hello(i=0):
    print(i, "Hello, world!")
    i += 1
    if i < 5:
        hello(i)  # RECURSIVE CALL
    else:
        return  # BASE CALL


hello()
