# # # Linkedlist

# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None

# #     def traverseAndPrint(self):
# #         currentNode = self

# #         while currentNode:
# #             print(currentNode.data, end="->")
# #             currentNode = currentNode.next
# #         print("null")


# # node1 = Node(7)
# # node2 = Node(11)
# # node3 = Node(3)
# # node4 = Node(9)


# # node1.next = node2
# # node2.next = node3
# # node3.next = node4

# # node1.traverseAndPrint()

# # Question 1: Build and traverse a linked list
# # Create a linked list containing these values:

# # 15 → 25 → 35 → 45 → null

# # Your tasks:

# # Create a Node class with data and next.

# # Create four nodes.

# # Connect the nodes together.

# # Write a traverseAndPrint() method inside the class.

# # Print the entire linked list.
# class LL:
#     def __init__(self,data):
#         self.data = data
#         self.tail = None

#     def traverseAndPrint(self):
#         currentNode = self

#         while currentNode:
#             print(currentNode.data, end="->")
#             currentNode = currentNode.tail
#         print("null")

# node1 = LL("15")
# node3 = LL("35")
# node2 = LL("25")
# node4 = LL("45")

# node1.tail = node2
# node2.tail = node3
# node3.tail = node4


# print(node1.traverseAndPrint())


# class LinkedLists():
#     def __init__(self,data):
#         self.data = data
#         self.tail = None 

#     def traverseandPrint(self):
#         currentNode = self

#         while currentNode:
#             print(currentNode.data, end = "->")
#             currentNode = currentNode.tail
#         print("null")

# node1 = LinkedLists(10)
# node3 = LinkedLists(30)
# node2 = LinkedLists(10)
# node5 = LinkedLists(50)
# node4 = LinkedLists(40)

# node1.tail = node2
# node2.tail = node3
# node3.tail = node4
# node4.tail = node5

# print(node1.traverseandPrint())
# rum = node1.traverseandPrint()
# node1.count()


class Linkedlists():
    def __init__(self,data):
        self.data = data
        self.tail = None

    def traverseAndPrint(self):
        currentNode = self
        while currentNode:
            print(currentNode.data, end ="->")
            currentNode = currentNode.tail # to avoid unlimited loop

    def count(self):
        count = 0
        currentNode = self

        while currentNode:
            count +=1 
            currentNode = currentNode.tail

        return count

node1 = Linkedlists(10)
node2 = Linkedlists(20)
node3 = Linkedlists(30)
node4 = Linkedlists(40)
node5 = Linkedlists(50)

node1.tail = node2
node2.tail = node3
node3.tail = node4
node4.tail = node5


print(node1.traverseAndPrint())
print("not valid")
print(node1.count())

