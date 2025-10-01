class Stack:
    def __init__(self):
        self.items=[]
    def push(self,k):
        self.items.append(k)
    def pop(self):
        if len(self.items)==0:
            print("Empty stack")
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            print("Stack is empty")
        else:
            return self.items[-1]
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    def display(self):
        return str(self.items)
y=Stack()
y.push("Talal")
y.push("Shahid")
print(y.peek())
print(y.pop())
print(y.size())
print(y.display())