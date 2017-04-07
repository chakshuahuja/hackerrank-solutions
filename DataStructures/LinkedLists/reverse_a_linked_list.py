# https://www.hackerrank.com/challenges/reverse-a-linked-list
"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    head = prev_node
    return head


def ReverseRecursiveUtil(item, tail=None):
    next = item.next
    item.next = tail
    if next is None:
        return item
    else:
        return ReverseRecursiveUtil(next, item)


def ReverseRecursive(head):
    if not head:
        return
    return ReverseRecursiveUtil(head)