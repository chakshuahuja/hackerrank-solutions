# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

from copy import deepcopy


def size(dup_head):
    count = 0
    while(dup_head):
        count += 1
        dup_head = dup_head.next
    return count


def GetNode(head, position):
    dup_head = deepcopy(head)

    length = size(dup_head)
    pos = length - 1 - position
    curr_pos = 0
    while(head and curr_pos != pos):
        head = head.next
        curr_pos += 1
    return head.data
