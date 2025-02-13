class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class IterativeSolution:
    def reverseList(self, head: ListNode | None = None) -> ListNode | None:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


class RecursiveSolution:
    def reverseList(self, head: ListNode | None = None) -> ListNode | None:
        if not head:
            return head

        if not head.next:
            newHead = head
        else:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead
