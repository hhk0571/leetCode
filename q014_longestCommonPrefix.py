#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret_str = ''
        ch_lists = [list(s) for s in strs]
        
        for ch_set in zip(*ch_lists):
            # print(ch_set)
            first_elem = ch_set[0] if ch_set else ''
            is_same_ch = True
            for elem in ch_set:
                if elem != first_elem:
                    is_same_ch = False
                    break
            if is_same_ch:
                ret_str += first_elem
            else:
                break

        return ret_str


if __name__ == "__main__":
    testcases=[
        (["flower","flow"   ,"flight"] , "fl" ),
        (["dog"   ,"racecar","car"   ] , ''   )
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.longestCommonPrefix(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 24 ms, faster than 86.43% of Python online submissions for Longest Common Prefix.
