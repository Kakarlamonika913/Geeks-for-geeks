#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        
        #Traversing the array elements.
        for i in range(n-2):
            #Taking two pointers. One at element after ith index and another
            #at the last index.
            l=i+1
            r=n-1
            
            while(l<r):
                
                curr_sum=A[i]+A[l]+A[r]
                
                #If sum of elements at indexes i, l and r is equal 
                #to required number, we return true.
                if(curr_sum==X):
                    return True
                    
                #Else if the sum is less than required number, it means we need
                #to increase the sum so we increase the left pointer l.
                elif(curr_sum<X):
                    l+=1
                    
                #Else the sum is more than required number and we need to
                #decrease the sum so we decrease the right pointer r.
                else:
                    r-=1
                    
        #returning false if no triplet sum equal to required number is present.            
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
