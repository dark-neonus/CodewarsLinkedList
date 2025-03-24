class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
def rec_reverse(head):
    if head.next is None:
        return head
    next_node = rec_reverse(head.next)
    current_node = next_node
    while current_node.next is not None:
        current_node = current_node.next
    head.next = None
    current_node.next = head
    return next_node

def reverse(head):
    if head is None:
        return None
    return rec_reverse(head)
