# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 使用快慢指針法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 建立快慢指針
        fast = slow = head
        # 避免空指針異常，fast.next.next 才不會有問題
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False
