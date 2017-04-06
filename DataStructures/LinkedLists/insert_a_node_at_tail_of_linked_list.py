# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list?h_r=next-challenge
"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


def Insert(head, data):
    new_node = Node(data)
    if not head:
        head = new_node
        return head
    curr_node = head
    while(curr_node.next):
        curr_node = curr_node.next
    curr_node.next = new_node
    return head
