class Deque():
    def __init__(self):
        self.a = []
    def isEmpty(self):
        return self.a == []
    def lpush(self, b):
        self.a.insert(0, b)
    def rpush(self, b):
        self.a.append(b)
    def rpop(self):
        return self.a.pop()
    def lpop(self):
        return self.a.pop(0)
    def size(self):
        return len(self.a)
    def rpeek(self):
        return self.a[len(self.a)-1]
    def lpeek(self):
        return self.a[0]

d = Deque()
word = input()
for letter in word:
    d.rpush(letter)
count = 0
flag = True
for i in range(len(d.a) // 2):
    if d.rpop() != d.lpop():
        flag = False
print(flag)