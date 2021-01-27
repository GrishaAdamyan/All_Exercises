class Queue():
    def __init__(self):
        self.a = []

    def isEmpty(self):
        return self.a == []

    def push(self, b):
        self.a.insert(0, b)

    def pop(self):
        return self.a.pop()

    def size(self):
        return len(self.a)

    def peek(self):
        return self.a[len(self.a)-1]

k = int(input())
n = int(input())
queue = Queue()
print(queue.isEmpty())
for i in range(1, k + 1, 1):
    queue.push(i)
print(queue.a)

count = 0
while queue.size() > 1:
    queue.push(queue.pop())
    count += 1
    if count == n:
        queue.pop()
        count = 0
print(queue.a[0])