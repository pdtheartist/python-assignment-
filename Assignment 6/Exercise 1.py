numbers = []

while True:
    num = input("Enter number: ")
    if num == "":
        break

    numbers.append(int(num))

numbers.sort()
numbers.reverse()

print("Five greatest numbers:", numbers[:5])