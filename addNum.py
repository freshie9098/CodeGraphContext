
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach : No need to reverse them as they are stored in reverse order!

        # just keep taking and adding post this with remainders.
        #Answer Node = 7
        # 9+9+rem = 18, number_for_node = 18%10 = 8, rem = number_for_node//10 = 1
        # 9+9+rem = 10, number_for_node = 0 , rem = 1, Answer Node = 0
        # 9+9+rem = 7+1 = 8, number_for_node = 8, rem = 0, Answer_node = 8

        #at the end check if more remainder are there, put them there.

        curr1 = l1
        curr2 = l2
        res = ListNode(0)
        res_head = res
        rem = 0
        while curr1 or curr2:
            num1 = num2 = 0
            if curr1:
                num1 = curr1.val
                curr1 = curr1.next

            if curr2:
                num2 = curr2.val
                curr2 = curr2.next
            
            number_node = (num1+num2+rem)%10
            res.next = ListNode(number_node)
            res = res.next
            rem = (num1+num2+rem)//10
        if rem:
            res.next = ListNode(rem)
            res = res.next

        return res_head.nexta
