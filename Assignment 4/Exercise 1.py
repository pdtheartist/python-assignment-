numbers = []

while True:
    s = input("Enter a number (empty to quit): ")
    if s == "":
        break
    numbers.append(float(s))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)
