# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        new_node = ListNode(0)
        node_tail = new_node
        while l1 or l2 or carry_over:
            l1_val = (l1.val if l1 else 0)
            l2_val = (l2.val if l2 else 0)
            carry_over, new_val = divmod(l1_val + l2_val + carry_over, 10)
            
            node_tail.next = ListNode(new_val)
            node_tail = node_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return new_node.next
