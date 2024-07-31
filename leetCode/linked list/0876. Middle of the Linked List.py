# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用快慢指針法(head動一個，current動兩個)
        curr = head
        # 當curr不存在和curr.next空值不會進入迴圈
        while curr and curr.next:
            head = head.next
            curr = curr.next.next
        return head
