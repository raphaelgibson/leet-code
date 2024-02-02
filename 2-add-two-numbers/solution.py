class Solution:
    def get_list_node_digits(self, list_node: ListNode) -> str:
        next_digits = ''

        if list_node.next is not None:
            next_digits = self.get_list_node_digits(list_node.next)

        return ''.join([str(list_node.val), next_digits])

    def make_list_node_from_digits(self, digits: str, original_list_node: Optional[ListNode] = None) -> ListNode:
        if original_list_node is None:
            list_node = ListNode(int(digits[0]))
        else:
            list_node = ListNode(int(digits[0]), original_list_node)

        if len(digits) > 1:
            return self.make_list_node_from_digits(digits[1:], list_node)

        return list_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_digits = int(self.get_list_node_digits(l1)[::-1])
        l2_digits = int(self.get_list_node_digits(l2)[::-1])
        sum_digits = str(l1_digits + l2_digits)
    
        return self.make_list_node_from_digits(sum_digits)
