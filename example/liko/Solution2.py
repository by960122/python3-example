class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        cursor = root
        carry = 0
        while (l1 or l2 or carry):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            cursor.next = ListNode(s % 10)
            cursor = cursor.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        return root.next
