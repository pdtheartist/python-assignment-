import math

def gia_don_vi(duong_kinh, gia):
    ban_kinh_met = (duong_kinh / 2) / 100
    dien_tich = math.pi * (ban_kinh_met ** 2)
    return gia / dien_tich

p1_d, p1_g = 30, 10
p2_d, p2_g = 45, 15

gia1 = gia_don_vi(p1_d, p1_g)
gia2 = gia_don_vi(p2_d, p2_g)

print(f"Giá mỗi m2: Pizza1 = {gia1:.2f}$, Pizza2 = {gia2:.2f}$")
if gia1 < gia2:
    print("Chọn Pizza 1 hời hơn!")
else:
    print("Chọn Pizza 2 hời hơn!")