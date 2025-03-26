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
    slow = node
    fast = node

    # Find intersection of slow and fast
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node

            # find start of loop
            while slow != fast:
                slow = slow.next
                fast = fast.next

            fast = fast.next
            loop_len = 1

            while fast != slow:
                fast = fast.next
                loop_len += 1

            return loop_len

    return 0
