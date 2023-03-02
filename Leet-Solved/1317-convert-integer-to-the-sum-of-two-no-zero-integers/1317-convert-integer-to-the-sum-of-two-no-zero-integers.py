class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' in str(i) or '0' in str(n-i):
                continue
            else:
                return [i, n-i]

'''
The method uses a loop to iterate over all integers i from 1 to n-1. For each i, it checks 
if both i and n-i are No-Zero integers by checking if '0' appears in their string representation. 
If either i or n-i contains '0', the loop skips to the next iteration using the continue keyword. 
If both i and n-i are No-Zero integers, the function returns a list containing i and n-i.
'''            

            
    