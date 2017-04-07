# https://www.hackerrank.com/challenges/compare-two-linked-lists
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    if (not headA) and (not headB):
        return True
    if (headA and (not headB)) or (headB and (not headA)):
        return False
    currA = headA
    currB = headB
    while(currA and currB):
        if currA.data == currB.data:
            currA = currA.next
            currB = currB.next
        else:
            return False
    if currA or currB:
        return False
    return True