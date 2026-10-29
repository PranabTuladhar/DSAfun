# x = [9,100,22,10,55,6,10,12,33,4]
# print(x)
# x.append(1)
# print(x)
# x.sort()
# print(x)
# x.remove(55)

# scores = [45,22,82,91,58]
# print(scores)
# scores.append(10)
# print(scores)
# scores.remove(58)
# scores.insert(2,72)
# print(scores)


class Numbers:
    def __init__(self,number):
        self.number = number

number1 = Numbers(1)
number2 = Numbers(4)
number3 = Numbers(4)
number4 = Numbers(4)
number4 = Numbers(4)
number5 = Numbers(4)

numberz = [number1,number2,number3,number4,number4,number5]
for number in numberz:
    print(number.number)
numberz.reverse()
numberz.index(1,numberz)
print("Seperation Section")
for number in numberz:
    print(number.number)
print(numberz.count(0))

for number in numberz:
    if number.number != 4:
        print("Number not found")
    else:
        print("Number 4 found")

