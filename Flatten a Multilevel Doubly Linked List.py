class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        stack = []
        curr = head
        
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            if not curr.next and stack:
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr
            
            curr = curr.next
        
        return head
