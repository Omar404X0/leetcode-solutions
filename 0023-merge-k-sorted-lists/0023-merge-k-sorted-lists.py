# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
      return None


    converted_lists = []
    for head in lists:
      current_list = []
      curr = head
      while curr:
        current_list.append(curr.val)
        curr = curr.next
      converted_lists.append(current_list)
    lists = converted_lists

    Big_list = []

    if type(lists[0]) == int:
      for num in lists:
        Big_list.append(num)

      Big_list = sorted(Big_list)

    else:
      x = 0
      while x < len(lists):
        for num in lists[x]:
          Big_list.append(num)
        x += 1
        Big_list = sorted(Big_list)

    if not Big_list:
      return None

    dummy = ListNode(0)
    curr = dummy
    for val in Big_list:
      curr.next = ListNode(val)
      curr = curr.next

    return dummy.next