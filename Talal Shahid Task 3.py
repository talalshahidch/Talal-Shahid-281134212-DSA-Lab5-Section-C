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
def reverse_string(s):
    stack = Stack()
    for i in s:
        stack.push(i)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

b=Stack()
b.push("Talal")
b.push("Shahid")
print(b.peek())
print(b.pop())
print(b.size())
print(b.display())
print(reverse_string("Goodbye"))