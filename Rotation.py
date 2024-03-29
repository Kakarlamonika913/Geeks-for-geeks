   low,high = 0, n-1
        
        while low<= high:
            mid = low +(high-low) // 2
            
            prev = (mid - 1+n) % n
            next = (mid + 1) % n
            
            if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
                return mid
            elif arr[mid] <= arr[high]:
                high = mid - 1
            elif arr[mid] >= arr[low]:
                low = mid + 1
        return 0
