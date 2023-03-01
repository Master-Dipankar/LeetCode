class Solution:
    def duplicateZeros(self, arr):
        """
        Duplicate each occurrence of zero, shifting the remaining elements to the right.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
'''
The function takes an integer array arr as input and modifies it in place by duplicating each occurrence of zero and shifting the remaining elements to the right.

The algorithm iterates through the array using a while loop and checks if the current element is equal to zero. If so, it inserts a zero after the current element using the insert() method and removes the last element of the array using the pop() method to maintain the fixed length of the array.

After inserting a zero and removing the last element, the algorithm increments the index by 1 to skip the newly inserted zero in the next iteration.
'''