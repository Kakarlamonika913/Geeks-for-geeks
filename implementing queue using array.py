class MyQueue(object):
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data) 

    def pop(self):
        if self.stack:
            return self.stack.pop(0) 
        return -1
