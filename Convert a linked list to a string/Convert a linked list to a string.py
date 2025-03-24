def stringify(node):
    current_node = node
    result = str(current_node.data if current_node is not None else None)
    while current_node != None:
        current_node = current_node.next
        result += f" -> {current_node.data if current_node is not None else None}"
    return result
