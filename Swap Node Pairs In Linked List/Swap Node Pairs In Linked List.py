from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    prev_node = Node(head)
    a_node = head
    b_node = head.next
    next_node = b_node.next
    
    head = b_node
    
    while b_node is not None:
        b_node.next = a_node
        a_node.next = next_node
        prev_node.next = b_node
        
        prev_node = a_node
        a_node = a_node.next
        if a_node is None:
            break
        b_node = a_node.next
        if b_node is None:
            break
        next_node = b_node.next
        
    return head
