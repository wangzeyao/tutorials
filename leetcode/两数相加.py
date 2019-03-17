
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(0)
node2 = node1
node2.next = ListNode(1)
node2 = node2.next
print(node1.next.val)

class Solution:
    def addTwoNumbers(self, l1, l2):
        out = ListNode(0)
        o = out
        carry = 0
        while (l1 or l2):  # 用and时候加括号
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum//10  # 向下取整
            o.next = ListNode(sum % 10)
            o = o.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            o.next = ListNode(1)
        return out.next
