class Solution:
    def findRestaurant(self, list1, list2):
        common = set(list1) & set(list2) # find common strings
        index_sum = {} # create a dictionary to store the index sums

        # calculate the index sums for each common string
        for c in common:
            index_sum[c] = list1.index(c) + list2.index(c)

        # find the minimum index sum
        min_sum = min(index_sum.values())

        # create a list of common strings with the minimum index sum
        result = [c for c in index_sum if index_sum[c] == min_sum]

        return result
    
'''
I first find the common strings betien the two lists using the set intersection operation &. i then create a dictionary to store the index sum for each common string by adding the index of the string in list1 and the index of the string in list2. I then find the minimum index sum and create a list of common strings that have the minimum index sum. Finally, i return this list as the result.
'''