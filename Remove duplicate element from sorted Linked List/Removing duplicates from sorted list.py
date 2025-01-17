class node:
    def deleteDuplicates(self,head:Optional[ListNode])-> Optional[ListNode]:
        current_node=head_node
        while current_node:
            while current_node.next and current_node.next.val == current_node.val:
                current_node.next=current_node.next.next
            current_node=current_node.next    
        return head    
