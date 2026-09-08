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
        m = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            m[cur] = copy
            cur = cur.next 
        cur = head 
        while cur:
            copy = m[cur]
            copy.next = m[cur.next]
            copy.random = m[cur.random]
            cur = cur.next 
        return m[head]