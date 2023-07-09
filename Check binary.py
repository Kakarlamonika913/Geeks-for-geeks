# Return true if str is binary, else false
def isBinary(str):
    #code here
    cnt = 0 
    for i in str:
        if( i=='0'or i=='1'):
            cnt+=1
    if(cnt==len(str)):
        return (True)
    return (False)


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends
