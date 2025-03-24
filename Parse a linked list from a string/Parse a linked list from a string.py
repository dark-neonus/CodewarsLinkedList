def linked_list_from_string(s):
    splited = s.split(" -> ")
    splited.reverse()
    current_node = None
    for data in splited:
        if data != "None":
            current_node = Node(int(data), current_node)
    return current_node