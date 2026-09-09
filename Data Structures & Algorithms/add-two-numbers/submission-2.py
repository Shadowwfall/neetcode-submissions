# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        carry = 0 
        while l1 or l2:
            sum = carry 
            if(l1):
                sum += l1.val 
                l1 = l1.next 
            if(l2):
                sum += l2.val 
                l2 = l2.next 
            cur.next = ListNode(sum%10)
            carry = sum // 10 
            cur = cur.next 
        if(carry): cur.next = ListNode(carry) 
        return ans.next