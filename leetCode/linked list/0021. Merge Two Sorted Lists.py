# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 創建一個虛擬節點
        dum = ListNode(-1)
        # 記錄頭節點
        ans = dum
        while list1 and list2:
            if list1.val <= list2.val:
                dum.next = list1
                list1 = list1.next
                dum = dum.next
            else:
                dum.next = list2
                list2 = list2.next
                dum = dum.next
            # 如果list1為空值，可以推論list2一定比較大
            if not list1:
                dum.next = list2
            elif not list2:
                dum.next = list1

            return ans.next
