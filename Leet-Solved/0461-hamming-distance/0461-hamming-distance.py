class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # convert integers to binary
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        
        # make binary strings equal length
        len_diff = abs(len(binary_x) - len(binary_y))
        if len(binary_x) > len(binary_y):
            binary_y = '0' * len_diff + binary_y
        else:
            binary_x = '0' * len_diff + binary_x
        
        # calculate Hamming distance
        hamming_distance = 0
        for i in range(len(binary_x)):
            if binary_x[i] != binary_y[i]:
                hamming_distance += 1
        
        return hamming_distance
