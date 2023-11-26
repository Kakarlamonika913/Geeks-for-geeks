if A == B:
            return 1
        elif C == 0:
            return 0
        n = (B - A + C)/C
        if n - int(n) == 0 and n > 0:
            return 1
        return 0

