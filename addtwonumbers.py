# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

result = "2019-10-09\nRuntime: 80 ms, faster than 5.25% of Python online submissions for Add Two Numbers.\nMemory Usage: 11.7 MB, less than 83.82% of Python online submissions for Add Two Numbers."

def popLast(l):
    """Pops last element of the list until there the end"""
    while(l.next is not None):
        prev  = l
        l = l.next
    prev.next = None
    return str(l.val)


def returnNumber(l):
    """Returns the reversed number from the list"""
    value_list = []
    while(True):
        if l.next is None:
            value_list.append(str(l.val))
            break
        else:
            value_list.append(popLast(l))
    return int(''.join(value_list))


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1, n2 = list(map(returnNumber, (l1, l2)))
    total = str(n1 + n2)
    total = ''.join(reversed(total))
    # Converts python string to ListNode single-linked list
    ln = ListNode(total[0])
    temp = ln
    for e in total:
        temp.next = ListNode(e)
        temp = temp.next
    return ln.next

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