# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    '''
    Case number one: the first node of the linked list has a value equal to k.
    This means that we actually need to modify the head of the linked list.
    
    There are two important conditions to modifying the head node:
        1. It is not None
        2. Its value is equal to k
    '''

    while l != None and l.value == k:
            l = l.next
    
    '''
    Case number two: any non-head node of the linked list has a value equal to k.
    This means that we need to modify node.next references to "skip over" the node which
    we need to delete.
    
    '''
    node = l # start from the head node
    while node != None:
        print(node) # access the node value
        if node.next != None:
            if node.next.value == k:       
                node.next = node.next.next # move on to the next node
        node = node.next
    
    return l 
