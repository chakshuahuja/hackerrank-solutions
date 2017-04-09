# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list
"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    if (not head) or (not head.next):
        return head
    curr_node = head
    prev_node = None
    while(curr_node):
        if not prev_node:
            prev_node = curr_node
            curr_node = curr_node.next
        elif prev_node.data == curr_node.data:
            prev_node.next = curr_node.next
            curr_node = curr_node.next
        else:
            prev_node = curr_node
            curr_node = curr_node.next
    return head