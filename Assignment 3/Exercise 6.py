def get_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]

# Chạy thử hàm
text = input("Nhập một chuỗi: ")
print("Ký tự ở giữa là:", get_middle(text))