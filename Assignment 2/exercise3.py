def check_hemoglobin(gioi_tinh, chi_so):
    if gioi_tinh.lower() == "nu":
        thap, cao = 117, 155
    else:
        thap, cao = 134, 167

    if chi_so < thap:
        kq = "Thấp"
    elif chi_so > cao:
        kq = "Cao"
    else:
        kq = "Bình thường"
    print(f"Giới tính: {gioi_tinh}, Chỉ số: {chi_so} -> Kết quả: {kq}")

check_hemoglobin("nu", 120)