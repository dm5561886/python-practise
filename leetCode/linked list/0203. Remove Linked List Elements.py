class ListNode:
    # val:儲存節點的值，next:指向下一個節點(存放下一個節點記憶體位置)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        # 判斷目前 curr 的值是否等於題目要求的值(是的話做刪除的動作)
        if curr.val == val:
            # 判斷目標值是不是在首節點
            if prev != None:  # 如果prev不等於空值，代表在節點的中間
                prev.next = curr.next
            else:  # prev為空值，代表是首節點
                head = curr.next  # return head節點會從第二個節點開始，代表刪除第一個
            curr = curr.next  # 刪除完之後繼續往前移動
        # 如果不是 prev先往前，curr再往前
        else:
            prev = curr
            curr = curr.next

    return head
