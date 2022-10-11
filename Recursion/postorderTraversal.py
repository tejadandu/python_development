root = {
    "data": "A",
    "children": [
        {"data": "B", "children": [{"data": "D", "children": []}]},
        {
            "data": "C",
            "children": [
                {
                    "data": "E",
                    "children": [
                        {"data": "G", "children": []},
                        {"data": "H", "children": []},
                    ],
                },
                {"data": "F", "children": []},
            ],
        },
    ],
}


def postorderTraverse(node):
    for child in node["children"]:
        # RECURSIVE CASE
        postorderTraverse(child)  # Traverse the child node
    print(node["data"], end=" ")  # Access the node's data
    # BASE CASE
    return


postorderTraverse(root)
