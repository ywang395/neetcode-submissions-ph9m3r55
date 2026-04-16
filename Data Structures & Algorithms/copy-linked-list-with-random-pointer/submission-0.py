"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random_dic = {None:None}
        curr = head 

        while curr : 
            copy = Node(curr.val)
            random_dic [curr] = copy 
            curr = curr.next
        curr = head 

        while curr: 
            copy = random_dic[curr]
            copy.next = random_dic[curr.next]
            copy.random = random_dic[curr.random]
            curr = curr.next 
        return random_dic [head]