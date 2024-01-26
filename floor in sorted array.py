 low = 0
        high = N-1
        while low<=high:
            mid=(low+high)//2
            if A[mid]>X:
                high=mid-1
            elif A[mid]==X:
                return mid
            else:
                if mid==N-1 or A[mid+1]>X:
                    return mid
                else:
                    low = mid+1
        return -1

..... see less

1

0
Reply
