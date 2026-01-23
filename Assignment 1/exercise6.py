# Gán giá trị đúng như ví dụ trong hình: 3 talents, 9 pounds, 13.5 lots
talents = 3
pounds = 9
lots = 13.5

# Quy tắc quy đổi
# 1 talent = 20 pound
# 1 pound = 32 lot
# 1 lot = 13.3 gram
total_grams = ((talents * 20 + pounds) * 32 + lots) * 13.3

kilograms = int(total_grams // 1000)
grams_left = total_grams % 1000

print(f"Enter talents: {talents}")
print(f"Enter pounds: {pounds}")
print(f"Enter lots: {lots}")
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams_left:.2f} grams.")
