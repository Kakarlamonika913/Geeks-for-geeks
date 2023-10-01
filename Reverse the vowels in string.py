#User function Template for python3



class Solution:

    def modify(self, s):

        # code here

        vowels='aeiou'

        x=""

        j=0

        y=""

        for i in s:

            if vowels.count(i):

                x=str(i)+x

            else:

                continue

        for i in s:

            if vowels.count(i):

                y+=x[j]

                j+=1

            else:

                y+=i

        return y





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        s = input().strip()

        ob = Solution()

        ans = ob.modify(s)

        print(ans)

# } Driver Code Ends
