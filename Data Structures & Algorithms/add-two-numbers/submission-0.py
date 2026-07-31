# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        result = None
        carry = 0
        total = 0

        while l1 and l2:
            total = l1.val+l2.val+carry
            carry = total//10
            temp = total%10
            if result is None:
                result = ListNode(temp)
                dummy = result
            else:
                result.next = ListNode(temp)
                result = result.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val+carry
            carry = total//10
            temp = total%10
            if not result:
                result = ListNode(temp)
            else:
                result.next = ListNode(temp)
                result = result.next
            l1 = l1.next

        while l2:
            total = l2.val+carry
            carry = total//10
            temp = total%10
            if result is None:
                result = ListNode(temp)
            else:
                result.next = ListNode(temp)
                result = result.next
            l2 = l2.next
        
        if carry:
            result.next = ListNode(carry)
            result = result.next
        print(dummy.val)
        return dummy
