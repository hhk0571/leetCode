#!/usr/bin/env python
# coding: utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            # print('n:',n, 'count_str: 1')
            return '1'

        tmp_str = self.countAndSay(n-1)

        last_ch  = ''
        last_cnt = 0
        new_str = ''
        for ch in tmp_str:
            if last_ch == '':
                last_ch = ch
            
            if ch == last_ch:
                last_cnt += 1
            else:
                new_str += '%d%s' %(last_cnt, last_ch)
                last_ch = ch
                last_cnt = 1
        else:
            new_str += '%d%s' %(last_cnt, last_ch)
        
        # print('n:',n, 'count_str:', new_str)
        return new_str
        

if __name__ == "__main__":
    testcases=[
        (1,'1'              ),
        (2,'11'             ),
        (3,'21'             ),
        (4,'1211'           ),
        (5,'111221'         ),
        (6,'312211'         ),
        (7,'13112221'       ),
        (8,'1113213211'     ),
        (9,'31131211131221' ),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.countAndSay(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 28 ms, faster than 44.68% of Python online submissions for Count and Say.
