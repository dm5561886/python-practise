# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 保存頭節點
        curr = head
        # 初始化前一個節點
        prev = None
        while curr:
            # 保存curr.next的節點
            temp = curr.next
            # 反轉，指向後面的節點
            curr.next = prev
            # 往前移動，作為反轉的點
            prev = curr
            # 保存 temp 節點
            curr = temp
        # 反轉後 prev會變頭節點
        return prev
