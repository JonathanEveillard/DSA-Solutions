class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty or single node list
        if head is None or head.next is None:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Flip the pointers
        head.next.next = head
        head.next = None
        
        # Return the new head of the reversed list
        return new_head
