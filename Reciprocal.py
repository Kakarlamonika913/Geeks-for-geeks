#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        ans=''
        for i in S:
            if ord(i)>=ord('a') and ord(i)<=ord('z'):
                i = chr(ord('z') - (ord(i) - ord('a')))
            elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
                i = chr(ord('Z') - (ord(i) - ord('A')))
            ans+=i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends
