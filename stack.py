class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


s=Stack()

print "Stack isEmpty ? ",s.isEmpty()
s.push(4)
s.push('dog')
s.push("orange")
s.push(8.4)
s.push("vikas")
print "Size of Stack : ",s.size()
print "Stack isEmpty ? ",s.isEmpty()
print s.pop()," is popped "
print s.pop()," is popped "
print "Size of Stack : ",s.size()
print "items in Stack : ",s.items