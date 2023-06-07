
import pprint
from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle special case that the list is empty
        if head == None:
            return head
        # Initialize curr with the address of head node...
        curr = head
        # Travel the list until the second last node
        while curr.next != None:
            # If the value of curr is equal to the value of prev...
            # It means the value is present in the linked list...
            if curr.val == curr.next.val:
                # Hence we do not need to include curr again in the linked list...
                # So we increment the value of curr...
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            # Otherwise, we increment the curr pointer...
            else:
                curr = curr.next
        # Return the sorted linked list without any duplicate element...
        pprint.pprint(vars(head))

        return head


head = [1, 1, 2]
# head = [1, 1, 2, 3, 3]
tmp = Solution()

out1 = tmp.deleteDuplicates(head)

print(out1)
