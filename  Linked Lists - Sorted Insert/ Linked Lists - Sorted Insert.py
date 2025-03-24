""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current_node = head
    if head.data >= new_node.data:
        new_node.next = head
        return new_node
    while current_node.next is not None:
        if current_node.next.data >= new_node.data:
            buffer = current_node.next
            current_node.next = new_node
            new_node.next = buffer
            return head
        current_node = current_node.next
    current_node.next = new_node
    return head
