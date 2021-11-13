# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if cur == None: return None
        
        while cur.next!= None:
            if cur.next.val == cur.val:
                if cur.next.next == None:
                    cur.next = None
                    return head
                else:
                    cur.next=cur.next.next

            else:
                cur = cur.next
        return head
