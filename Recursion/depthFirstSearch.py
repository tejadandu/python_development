root = {
    "name": "Alice",
    "children": [
        {"name": "Bob", "children": [{"name": "Darya", "children": []}]},
        {
            "name": "Caroline",
            "children": [
                {
                    "name": "Eve",
                    "children": [
                        {"name": "Gonzalo", "children": []},
                        {"name": "Hadassah", "children": []},
                    ],
                },
                {"name": "Fred", "children": []},
            ],
        },
    ],
}


def find8LetterName(node):
    print("visiting a node " + node["name"] + "...")

    # # Preorder depthfirst search:
    print("Checking if " + node["name"] + " is 8 letters...")
    if len(node["name"]) == 8:
        return node["name"]  # BASE CASE

    if len(node["children"]) > 0:
        # RECURSIVE CASE
        for child in node["children"]:
            returnValue = find8LetterName(child)
            if returnValue != None:
                return returnValue


    # Postorder depthfirst search
    # print("Checking if " + node["name"] + " is 8 letters...")
    # if len(node["name"]) == 8:
    #     return node["name"]  # BASE CASE
    # # Value is not found or there is no children.
    return None  # BASE CASE


print("Found an 8 letter word " + str(find8LetterName(root)))
