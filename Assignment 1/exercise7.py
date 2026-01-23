import random

# Tạo mã 3 chữ số từ 0-9
code1 = "".join([str(random.randint(0, 9)) for _ in range(3)])

# Tạo mã 4 chữ số từ 1-6
code2 = "".join([str(random.randint(1, 6)) for _ in range(4)])

print(f"Mã 3 chữ số ngẫu nhiên (0-9): {code1}")
print(f"Mã 4 chữ số ngẫu nhiên (1-6): {code2}")
