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


def inorderTraverse(node):
    if len(node["children"]) >= 1:
        # RECURSIVE CASE
        inorderTraverse(node["children"][0])
    print(node["data"], end=" ")
    if len(node["children"]) >= 2:
        # RECURSIVE CASE
        inorderTraverse(node["children"][1])
    # BASE CASE
    return


inorderTraverse(root)
