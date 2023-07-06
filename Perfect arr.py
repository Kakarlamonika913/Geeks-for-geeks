#User function Template for python3



class Solution:

    def IsPerfect(self,arr,n):

        #Complete the function

        arr1=arr[::-1]

        if arr==arr1:

            return True

        else:

            return False







#{ 

 # Driver Code Starts

#Initial Template for Python 3





for _ in range(0,int(input())):

    n = int(input())

    arr = list(map(int,input().strip().split()))

    ob=Solution()

    if(ob.IsPerfect(arr,n)):

        print("PERFECT")

    else:

        print("NOT PERFECT")

    

# } Driver Code Ends
