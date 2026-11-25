'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
# https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        node = Node(x)
        if head is None:
            return node
        
        else:
            curr = head
            while (curr.next != None):
                curr = curr.next
            curr.next = node
        return head
        
"""
T.C -> O(n)
S.C -> O(1)
Approach: Iterative Traversal

"""