def caesar_cipher(file_name, shift, direction):
    n = shift if direction.lower() == 'right' else -shift
    ciphertext = ""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        for char in content:
            if 'A' <= char <= 'Z':
                ciphertext += chr((ord(char) + n - 65) % 26 + 65)
            elif 'a' <= char <= 'z':
                ciphertext += chr((ord(char) + n - 97) % 26 + 97)
            else:
                ciphertext += char

        with open("ciphertext.txt", "w", encoding='utf-8') as output_file:
            output_file.write(ciphertext)
        print("Success! Please open 'ciphertext.txt' to see the result.")
    except FileNotFoundError:
        print("Error: input.txt not found.")
caesar_cipher("input.txt", 3, "right")