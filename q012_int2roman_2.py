#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    symbol = {
        1:    'I',    
        2:    'II',   
        3:    'III',  
        4:    'IV',   
        5:    'V',    
        6:    'VI',   
        7:    'VII',  
        8:    'VIII', 
        9:    'IX',   
        10:   'X',    
        20:   'XX',   
        30:   'XXX',  
        40:   'XL',   
        50:   'L',    
        60:   'LX',   
        70:   'LXX',  
        80:   'LXXX', 
        90:   'XC',   
        100:  'C',    
        200:  'CC',   
        300:  'CCC',  
        400:  'CD',   
        500:  'D',    
        600:  'DC',   
        700:  'DCC',  
        800:  'DCCC', 
        900:  'CM',   
        1000: 'M',    
        2000: 'MM',   
        3000: 'MMM',  
    }

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        place = 0
        lst =[]
        while num:
            num, mod = divmod(num, 10)
            roman = self.symbol.get(mod * (10**place))
            if roman:
                lst.insert(0, roman)
            place +=1
        
        return ''.join(lst)


if __name__ == "__main__":
    testcases=[
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('XII', 12),
        ('VIII', 8),
        ('XXVII', 27),
        ('LVIII', 58),
        ('CII', 102),
        ('CXCIX', 199),
        ('MCMXCIV', 1994),
        ('MMMCCCXXXIII', 3333),
        ('MCDXXXVII', 1437),

    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.intToRoman(testcase[1])
        print(i, 'OK' if ans == testcase[0] else 'Failed', 'expected:%s, given:%s'%(testcase[0], ans))

# Runtime: 72 ms, faster than 81.18% of Python online submissions for Integer to Roman.
