# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def InsertNth(head, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head
    curr_node = head
    prev_node = None
    curr_pos = 0
    while(curr_node and curr_pos != position):
        curr_pos += 1
        prev_node = curr_node
        curr_node = curr_node.next

    prev_node.next = new_node
    new_node.next = curr_node
    return head
