# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

result = "2019-10-09\nRuntime: 48 ms, faster than 92.75% of Python online submissions for Add Two Numbers.\nMemory Usage: 11.9 MB, less than 14.71% of Python online submissions for Add Two Numbers."


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Traversing lists, adding and creating final list all at the same time
    ln = ListNode("")
    temp = ln
    carry = 0
    while l1 is not None or l2 is not None or carry:
        #Traverse both lists and add to total of said Node
        if l1 is not None:
            carry += l1.val
            l1 = l1.next
        if l2 is not None:
            carry += l2.val
            l2 = l2.next
        temp.next = ListNode(carry%10)  # Get first digit of the number by modulus division
        temp = temp.next
        carry = carry//10               # Get the second digit of the number by flooring the number
    return ln.next                      # Returns next to eliminate the dummy first value


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == "__main__":
    listnode1 = ListNode(2)
    listnode1.next = ListNode(4)
    listnode1.next.next = ListNode(3)
    listnode2 = ListNode(5)
    listnode2.next = ListNode(6)
    listnode2.next.next = ListNode(4)

    addTwoNumbers(listnode1, listnode2)
    print(result)