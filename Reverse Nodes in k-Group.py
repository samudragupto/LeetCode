class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_start = prev_group_end.next
            group_next = kth.next
            
            # Reverse group
            prev, curr = kth.next, group_start
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect reversed group
            temp = prev_group_end.next
            prev_group_end.next = kth
            prev_group_end = temp
