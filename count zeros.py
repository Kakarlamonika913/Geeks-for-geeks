class Solution:
    def countZeroes(self, arr, n):
        # code here
        if 0 not in arr:
            return 0
        return (n - arr.index(0))
