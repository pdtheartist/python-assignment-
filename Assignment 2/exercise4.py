def la_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"{nam} là năm nhuận.")
    else:
        print(f"{nam} không phải năm nhuận.")

la_nam_nhuan(2026)