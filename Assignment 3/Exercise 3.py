numbers = []
while True:
    val = input("Nhập một số (nhấn Enter để kết thúc): ")
    if val == "":
        break
    numbers.append(float(val))

if numbers:
    print(f"Số lớn nhất: {max(numbers)}")
    print(f"Số nhỏ nhất: {min(numbers)}")
