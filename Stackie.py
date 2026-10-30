# # Question 1 — Basic stack operations
# # You are building a stack of books. Create an empty list called books and:

# # Push "Harry Potter", "The Hobbit", and "Dune" onto the stack.

# # Remove the top book from the stack.

# # Print the book you removed.

# # Print the remaining stack.

# # Hint: In Python, .append() pushes an item onto a stack, and .pop() removes and returns the top item.


# # stack = []

# # stack.append('Harry Potter')
# # stack.append('The Hobbit')
# # stack.append('Dune')
# # stack.pop()
# # print(stack)

# # topElement = stack[-1]
# # print("Peek:",topElement)

# Question 2 — Predict and code
# A stack starts empty. Perform these operations in order:

# Push 10.

# Push 20.

# Push 30.

# Pop the top item and store it in a variable called removed.

# Push 40.

# Pop the top item again.

# Write the Python code and print:

# The two removed values.

# The final stack.

# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)
# removed1 = stack.pop()
# stack.append(40)
# removed2 = stack.pop()
# removed = [removed1,removed2]

# print(f"Removed items from stack:{removed}")
# print(f"Stack items:{stack}")

# Create a stack called numbers containing:


# python
# numbers = [5, 10, 15, 20, 25]
# Write a program that:

# Keeps popping items while the stack is not empty.

# Prints each item as it is removed.

# Counts how many items were popped.

# Prints the total number of items removed at the end.

# Extra challenge: Can you modify the program so it stops when it pops the number 15?
numbers = [5,10,15,20,25]

for number in numbers:
    while number:
        removed = numbers.pop()
        if removed == 10:
            break
        print(f"{removed} has been removed")
        # print(numbers.count())
    else:
        print("All items have been popped")