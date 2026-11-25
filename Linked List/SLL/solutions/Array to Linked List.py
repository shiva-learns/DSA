''' Linked List Node Structure
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
#  https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1


class Solution:
    def arrayToList(self, arr: list[int]) -> 'Node': #type: ignore
        # code here
        n = len(arr)

        head = Node(arr[0]) #type: ignore
        temp = head
        for i in range(1,n):
            new_node = Node(arr[i]) #type: ignore
            temp.next = new_node
            temp = new_node
            
        return head
"""
T.C -> O(n)
S.C -> O(1)
Approach: Linked List

"""