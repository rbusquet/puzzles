from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        if head.next is None:
            return head

        new_head = head.next

        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head
