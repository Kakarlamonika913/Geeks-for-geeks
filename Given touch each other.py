#User function Template for python3

class Solution:
    def circleTouch(self,X1,Y1,R1,X2,Y2,R2):
        #we are comparing squared values because sqrt leads to loss of precision sometimes.
        distanceBetweenCentresSquared=(X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1)
        sumOfRadiiSquared=(R2+R1)*(R2+R1)
        return (int)(distanceBetweenCentresSquared<=sumOfRadiiSquared)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        X1,Y1,R1,X2,Y2,R2=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.circleTouch(X1,Y1,R1,X2,Y2,R2))
# } Driver Code Ends
