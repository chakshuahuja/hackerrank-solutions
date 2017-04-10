# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node
   def __repr__(self):
       curr_node = self
       repr = ''
       while curr_node:
         repr += '%s->' % curr_node.data
         curr_node = curr_node.next
       return repr
 return the head node of the updated list 
"""


def SortedInsert(head, data):
    if not head:
        return Node(data)
    if not head.next:
        if head.data > data:
            new_node = Node(data, next_node=head)
            head.prev = new_node
            head = new_node
        else:
            new_node = Node(data, next_node=None, prev_node=head)
            head.next = new_node
        return head
    curr_node = head
    prev_node = None
    while(curr_node):
        if curr_node.data <= data:
            prev_node = curr_node
            curr_node = curr_node.next
        else:
            if not prev_node:
                new_node = Node(data, next_node=head)
                head.prev = new_node
                return new_node
            new_node = Node(data, next_node=curr_node, prev_node=prev_node)
            prev_node.next = new_node
            curr_node.prev = new_node
            return head
    new_node = Node(data, next_node=None, prev_node=prev_node)
    prev_node.next = new_node
    return head