from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None or index < 0:
        raise Exception()
    current_index = 0
    current_node = node
    while current_index < index:
        if current_node.next is None:
            raise Exception()
        current_index += 1
        current_node = current_node.next
    return current_node
  