while True:
    inch_input = float(input("Nhập giá trị inch (nhập số âm để dừng): "))
    if inch_input < 0:
        print("Chương trình kết thúc.")
        break
    cm = inch_input * 2.54
    print(f"{inch_input} inch = {cm} cm")