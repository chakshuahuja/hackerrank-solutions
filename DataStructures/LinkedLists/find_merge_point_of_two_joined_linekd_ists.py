# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

"""


def FindMergeNode(headA, headB):
    currA = headA
    while(currA):
        currB = headB
        while(currB):
            if(currB and currB.data == currA.data):
                return currB.data
            else:
                currB = currB.next
        currA = currA.next
