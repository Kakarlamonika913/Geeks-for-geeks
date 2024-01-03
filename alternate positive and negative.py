 pos_arr = []
        neg_arr = []
        for i in arr:
            if i>=0:
                pos_arr.append(i)
            
            else:
                neg_arr.append(i)
        arr.clear()
        
        limit = max(len(pos_arr),len(neg_arr))
        for i in range(limit):
            if i<len(pos_arr):
                arr.append(pos_arr[i])
                
            if i<len(neg_arr):
                arr.append(neg_arr[i])
        return arr

