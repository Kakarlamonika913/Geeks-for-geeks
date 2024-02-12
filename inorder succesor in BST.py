successor = None
        while root is not None:
            if x.data >= root.data:
                root = root.right
                
            else:
                successor = root
                root = root.left
                
        return successor
 
