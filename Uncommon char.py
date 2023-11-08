#User function Template for python3



class Solution:

    def UncommonChars(self,A, B):

        #code here

        s1=set(A).difference(B)

        s2=set(B).difference(A)

        li=sorted(s1.union(s2))

        new_s="".join(li)

        if (len(new_s)==0):

            return -1

        return new_s





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

    T = int(input())



    for tcs in range(T):

        A = input()

        B = input()

        ob = Solution()

        print(ob.UncommonChars(A, B))



# } Driver Code Ends
