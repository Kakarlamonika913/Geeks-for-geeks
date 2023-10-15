#User function Template for python3
import re
class Solution:

    def extractIntegerWords(self, s):
        # code here
        n=re.compile('[0-9]+')
        k=n.findall(s)
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        if solObj.extractIntegerWords(s):
            print(*solObj.extractIntegerWords(s))
        else:
            print("No Integers")

# } Driver Code Ends
