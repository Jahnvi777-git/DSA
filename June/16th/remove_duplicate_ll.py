# link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=problem-list-v2&envId=d5qblqpi
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = ListNode(777)
        prev.next = head
        t = prev
        cur = head
        while cur:
            if cur and cur.next and cur.val == cur.next.val:
                v = cur.val
                while cur and cur.val == v:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
            
        return t.next