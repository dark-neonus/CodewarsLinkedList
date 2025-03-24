from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    result = Node(data)
    result.next = head
    return result

def build_one_two_three():
    result = Node(3)
    result = push(result, 2)
    result = push(result, 1)
    return result