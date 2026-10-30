# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, element):
#         self.queue.append(element)

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue[0]

#     def isEmpty(self):
#         return len(self.queue) == 0

# myQueue = Queue()

# myQueue.enqueue('Aooh')
# myQueue.enqueue('Boo')
# myQueue.enqueue('Cooh')
# myQueue.enqueue('Doo')

# print(myQueue.queue)
# print(myQueue.peek())

# myQueue.dequeue()
# print(myQueue.queue)

# Question 1 — Basic Queue Operations
# Create a class called Queue with the following methods:

# enqueue() – adds an element to the queue.

# dequeue() – removes the first element.

# peek() – displays the first element without removing it.

# size() – returns the number of elements.

# Your task:

# Create an empty queue.

# Add 5 names to the queue.

# Print the queue.

# Remove two people from the queue.

# Print the queue again.

# Print the current size.

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self,element):
#         self.queue.append(element)

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue[0]

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def size(self):
#         return len(self.queue)

# myQueue = Queue()

# myQueue.enqueue("Person1")
# myQueue.enqueue("Person2")
# myQueue.enqueue("Person3")
# myQueue.enqueue("Person4")
# myQueue.enqueue("Person5")
# print(myQueue.queue)
# myQueue.dequeue()
# myQueue.dequeue()
# print(myQueue.queue)
# print(myQueue.size())


# Question 2 — Queue Management System
# Imagine you're creating a queue system for a supermarket checkout.

# Create a Queue class and:

# Add five customers to the queue.

# Print the first customer waiting.

# Remove the first customer after they have been served.

# Add two new customers.

# Print the updated queue.

# Check whether the queue is empty.
# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self,element):
#         self.queue.append(element)

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue[0]

#     def isEmpty(self):
#         return len(self.queue) == 0

# customers = Queue()

# customers.enqueue("Customer1")
# customers.enqueue("Customer2")
# customers.enqueue("Customer3")
# customers.enqueue("Customer4")
# customers.enqueue("Customer5")

# print(customers.queue)
# customers.dequeue()
# print(customers.queue)
# customers.enqueue("Customer6")
# customers.enqueue("Customer8")
# print(f"Peeking: {customers.peek()}")
# print(customers.queue)
# print(customers.isEmpty())


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        self.queue[0]

    def isEmpty(self):
        return len(self.queue == 0)

    