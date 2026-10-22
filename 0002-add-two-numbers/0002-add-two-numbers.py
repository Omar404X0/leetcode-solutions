class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        list_1 = []
        node = l1
        while node:
            list_1.append(node.val)
            node = node.next

        list_2 = []
        node = l2
        while node:
            list_2.append(node.val)
            node = node.next

        l1 = list_1
        l2 = list_2

        l1_str = ''
        l2_str = ''
        l = len(l1) - 1
        while l >= 0:
            l1_str = l1_str + str(l1[l])
            l -= 1

        l = len(l2) - 1
        while l >= 0:
            l2_str = l2_str + str(l2[l])
            l -= 1

        result = str(int(l1_str) + int(l2_str))

        final_list = []

        num = len(result) - 1

        while num >= 0:
            final_list.append(int(result[num]))
            num -= 1

        head = ListNode(final_list[0])
        current = head
        i = 1
        while i < len(final_list):
            current.next = ListNode(final_list[i])
            current = current.next
            i += 1

        return head