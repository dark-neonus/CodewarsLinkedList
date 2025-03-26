""" Idea for solution:
Find the starting point of loop in the Linked list
Given the problem, if there is a loop in the list, find the starting point where loop has started.
In the following example, the loop has started from node 20. We have to return the node.


One brute-force way of doing this problem would be, maintaining a hashmap of nodes visited.
If you visit the node again, which you will, in case of a loop. That node is going to be our first
node of the loop.

As the above method will take O(N) space complexity of using a map, so to further optimize
this code, we can use fast and slow pointer methods.

The approach will be almost the same as the previous one, we have to move
fast by two-step and slow by 1. when fast and slow meet, It’s not necessary that they will
meet at the start of the cycle.

So to find the starting point. When they meet, point start to head again, and move fast
by 1 step and slow by 1 step. And finally they will meet at the starting point of cycle.
"""



def loop_size(node):
    if node is None:
        raise Exception()
    if node == node.next:
        return 1
    if node.next is None or node.next.next is None:
        return 0
        
