#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i = 0
        j = 0
        k = 0 
        
        last = -12345678    #variable to store last common element
        res = []    #list to store the common elements
        
        #iterating through all three arrays
        while i < n1 and j < n2 and k < n3:
            
            #if the current element is common to all three arrays
            if A[i] == B[j] == C[k]:
                
                #checking if the common element is not already present
                if last != A[i]:
                    res.append (A[i])   #adding the common element to the result list
                    last = A[i]    #updating the last common element
                i += 1
                j += 1
                k += 1
            
            #if the minimum element is from the first array
            elif min (A[i], B[j], C[k]) == A[i]:
                i += 1   #incrementing the pointer for the first array
            
            #if the minimum element is from the second array
            elif min (A[i], B[j], C[k]) == B[j]:
                j += 1   #incrementing the pointer for the second array
            
            #if the minimum element is from the third array
            else:
                k += 1   #incrementing the pointer for the third array
                
        return res   


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends
