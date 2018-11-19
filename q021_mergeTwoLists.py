#!/usr/bin/env python
# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1 = listnode2list(l1)
        list_2 = listnode2list(l2)

        merged_list = list_1 + list_2

        return list2listnode(sorted(merged_list))


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
        ([1, 2, 4], [1,3,4], [1,1,2,3,4,4  ]),

    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.mergeTwoLists(list2listnode(tc[0]), list2listnode(tc[1]))
        print(i, 'OK' if listnode2list(ans) == tc[2] else 'Failed', 'expected:%s, return:%s'%(tc[2], listnode2list(ans)))

# Runtime: 36 ms, faster than 23.51% of Python online submissions for Merge Two Sorted Lists.
