# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if position == 0:
        head = head.next
        return head
    curr_node = head
    prev_node = None
    curr_pos = 0
    while(curr_node and curr_pos != position):
        curr_pos += 1
        prev_node = curr_node
        curr_node = curr_node.next
    prev_node.next = curr_node.next
    return head
