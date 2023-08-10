#User function Template for python3

class Solution:

    def convert(self, s):
        # code here
        ans=''
        for i in s:
            if ord(i) >= ord('a') and ord(i) <= ord('z'): 
                ans += chr(ord('z') - (ord(i) - ord('a')))
            else:
                ans += chr(ord('Z') - (ord(i) - ord('A')))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
# } Driver Code Ends
