class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()
    index = 0
    a_list = head
    last_a = a_list
    b_list = head.next
    last_b = b_list
    
    current_node = head.next.next
    
    while current_node is not None:
        if index % 2 == 0:
            last_a.next = current_node
            last_a = current_node
        else:
            last_b.next = current_node
            last_b = current_node
        current_node = current_node.next
        index += 1
    
    last_a.next = None
    last_b.next = None
    
    return Context(a_list, b_list)