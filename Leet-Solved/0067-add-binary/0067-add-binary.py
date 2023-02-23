class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a, 2)
        n2 = int(b, 2)
        b1 = bin(n1)
        b2 = bin(n2)
        addBinary = bin(int(b1, 2)+ int(b2, 2))[2:]
        '''addBinary = bin(int(a, 2)+ int(b2, 2))[2:]'''
        return(addBinary)