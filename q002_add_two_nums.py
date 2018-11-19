#!/usr/bin/env python
# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=l1
        b=l2
        result = c = ListNode(None)
        carry=0
        while a or b:
            av = a.val if a else 0
            bv = b.val if b else 0
            x = av + bv + carry
            c.next = ListNode(x % 10)
            carry = 1 if x >= 10 else 0
            if a: a = a.next
            if b: b = b.next
            c = c.next
        
        if carry: c.next = ListNode(carry)
        
        return result.next


def list2listnode(nums):
    lstnode = ListNode(None)
    curr_node = lstnode
    for n in nums:
        curr_node.next = ListNode(n)
        curr_node = curr_node.next
    return lstnode.next


def listnode2list(lstnode):
    lst = []
    while lstnode:
        lst.append(lstnode.val)
        lstnode = lstnode.next
    return lst


if __name__ == "__main__":
    testcases=[
        ([2, 4, 3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        ([1, 2, 7], [8,9], [9, 1, 8]),

    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.addTwoNumbers(list2listnode(testcase[0]), list2listnode(testcase[1]))
        print(i, 'OK' if listnode2list(ans) == testcase[2] else 'Failed', 'expected:%s, return:%s'%(testcase[2], listnode2list(ans)))

# Runtime: 68 ms, faster than 93.39% of Python online submissions.
