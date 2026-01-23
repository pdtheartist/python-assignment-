def kiem_tra_zander(chieu_dai):
    han_muc = 42
    if chieu_dai >= han_muc:
        print(f"Cá dài {chieu_dai}cm. Đủ tiêu chuẩn!")
    else:
        thieu = han_muc - chieu_dai
        print(f"Cá dài {chieu_dai}cm. Thả cá về hồ, thiếu {thieu}cm nữa.")

kiem_tra_zander(37)