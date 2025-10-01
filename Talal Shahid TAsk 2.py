class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty-")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


a= Queue()
a.enqueue('Ahmad')
a.enqueue('Muneeb')
a.enqueue('Talal')
print("Front element:", a.front())
print("Dequeued:", a.dequeue())
print("Dequeued:", a.dequeue())
print("Is empty:", a.is_empty())
print("Size:", a.size())
