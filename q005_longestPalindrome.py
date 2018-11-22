#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # make new string with odd length so that always has center position
        new_s = '#' + '#'.join(s) +'#'
        new_s_len = len(new_s)
        RL = [0] * new_s_len
        for i in range(new_s_len):
            for n in range(1, min(i, new_s_len -1-i)+1):
                if new_s[i-n ] == new_s[i+n]:
                    RL[i] += 1
                    # print(i,new_s[i], n, RL[i])
                else:
                    # print(i,new_s[i], n, RL[i])
                    break

        # print(', '.join(s))
        # print(RL)
        max_RL = max(RL)
        pos    = RL.index(max_RL)//2
        start  = pos -max_RL//2

        return s[start:start+max_RL]

## solution:
# [#, 1, #, 2, #, 3, #, a, #, b, #, c, #, d, #, c, #, b, #, a, #, e, #, e, #, e, #]
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 7, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 2, 1, 0]
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

# 0  1  2  3  4  5  6  7  8  9  10 11 12
# 1, 2, 3, a, b, c, d, c, b, a, e, e, e

# index = index_of_new_str//2
# start = index - max_value_index //2
# end = start + max_value


if __name__ == "__main__":
    testcases = [
        ('abcba'   , 'abcba'), 
        ('abccba'   , 'abccba'),
        ('abcdcbaeee'   , 'abcdcba'),
        ('123abcdcbaeee', 'abcdcba'),
        ('123abcdcba'   , 'abcdcba'),
        ('a'        , 'a'       ),
        ('123ea'        , '1'       ),
        ("klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc", 'wnsnw'),
        ("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg", 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'),
    ]

    solution = Solution()
    # print(solution.is_Palindrome('abcdcba'))
    # print(solution.is_Palindrome('abcdc'))
    for i, tc in enumerate(testcases):
        ans = solution.longestPalindrome(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 1008 ms, faster than 51.04% of Python online submissions for Longest Palindromic Substring.
