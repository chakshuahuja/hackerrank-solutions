# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list
"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def ReverseUtil(item, tail=None):
    next = item.next
    item.next = tail
    if tail:
        tail.prev = item
    if next is None:
        return item
    return ReverseUtil(next, item)


def Reverse(head):
    if (not head) or (not head.next):
        return head
    return ReverseUtil(head)
