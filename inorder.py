  a = []
        if root != None:
            a += self.InOrder(root.left)
            a.append(root.data)
            a += self.InOrder(root.right)
            
        return a
