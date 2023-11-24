class Solution:
    def firstRep(self, s):
        # code here
        char=-1
        for i in s:
            if s.count(i)>=2:
                char=i
                break
        return char
