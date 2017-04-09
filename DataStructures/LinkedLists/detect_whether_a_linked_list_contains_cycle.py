# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head or (not head.next):
        return 0
    curr_node = head
    list_size = 0
    while(curr_node and list_size <= 100):
        list_size += 1
        curr_node = curr_node.next
    if not curr_node:
        return 0
    else:
        return 1
