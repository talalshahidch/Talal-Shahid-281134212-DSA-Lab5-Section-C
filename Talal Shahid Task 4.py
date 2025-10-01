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
def valid_parenthesis(expression):
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()

    for char in expression:
        if char in brackets.keys():  
            stack.push(char)
        elif char in brackets.values():  
            if stack.is_empty():  
                return False
            top = stack.pop()
            if brackets[top] != char:
                return False

    return stack.is_empty() or True



print(valid_parenthesis("(Talal)"))
print(valid_parenthesis("{[()]}")) 
print(valid_parenthesis("{[(])}"))