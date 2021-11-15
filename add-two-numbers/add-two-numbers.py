# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(None,None)
        carry = 0
        while l1 or l2:
            if l1:
                dig1 = l1.val
                l1 = l1.next

            else:
                dig1 = 0

        
            if l2:
                dig2 = l2.val
                l2 = l2.next

            else:
                dig2 = 0

 
            sum_val = (carry+dig1+dig2)%10
            
            carry = (carry+dig1+dig2)//10
            
            if l3.val == None:
                l3.val = sum_val
                head = l3
            else:
                l3.next = ListNode(sum_val,None)
                l3 = l3.next
                
        if carry:
            l3.next = ListNode(1,None)
            
        return head