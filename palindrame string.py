 low = 0
        high = len(S)-1
        
        while low < high:
            
            if S[low] == S[high]:
                low += 1
                high -= 1
            else:
                return 0
          
        return 1
