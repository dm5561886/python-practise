class ListNode:
    # val:儲存節點的值，next:指向下一個節點(存放下一個節點記憶體位置)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)


node1.next = node2  # node1 next位置指向 node2節點
node2.next = node3
node3.next = node4
head = node1  # 代表整個串列的開頭

current_node = head  # 在leetcode中要再設一個current變數給head


# 查找節點
# while current_node:
#    if current_node.val == 3:
#        print("find")
#        break
#    current_node = current_node.next

# 插入節點資料
# current = head
# while current:
#    if current.val == 2:
#        new_node = ListNode(4)
#        new_node.next = current.next
#        current.next = new_node
#        break
#    current = current.next

# 刪除節點操作
current = head
previous = None
while current:
    if current.val == 3:
        if previous:
            previous.next = current.next
        else:
            head = current.next
        break
    previous = current
    current = current.next


# 遍歷節點
while current_node:
    print(current_node.val)
    current_node = current_node.next
