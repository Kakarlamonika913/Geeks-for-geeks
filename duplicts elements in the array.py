 from collections import Counter
        new = dict(Counter(arr))
        elem = []
        for key in new:
            if new[key] > 1:
                elem.append(key)
        
        if len(elem) == 0:
            return [-1]
        else:
            return sorted(elem)
