# link: https://leetcode.com/problems/reorder-list/description/
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        temp = slow.next
        slow.next = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        first = head
        second = prev

        while second:

            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2