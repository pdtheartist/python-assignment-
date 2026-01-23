def mo_ta_cabin(hang_cabin):
    if hang_cabin == "LUX":
        print("LUX: cabin tầng trên có ban công.")
    elif hang_cabin == "A":
        print("A: trên boong xe, có cửa sổ.")
    elif hang_cabin == "B":
        print("B: cabin không cửa sổ trên boong xe.")
    elif hang_cabin == "C":
        print("C: cabin không cửa sổ dưới boong xe.")
    else:
        print("Hạng cabin không hợp lệ")

mo_ta_cabin("B")