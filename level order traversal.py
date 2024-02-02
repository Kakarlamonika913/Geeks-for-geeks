d = deque([root])
        res = []
        while d:
            temp = d.popleft()
            res.append(temp.data)
            if temp.left:
                d.append(temp.left)
            if temp.right:
                d.append(temp.right)
        return res
