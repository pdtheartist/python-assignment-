def make_acronym(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

# Chạy thử hàm
text = input("Nhập cụm từ cần viết tắt: ")
print("Kết quả:", make_acronym(text))