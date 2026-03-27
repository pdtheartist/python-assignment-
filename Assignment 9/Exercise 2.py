def find_keyword_lines(file_name, keyword):
    line_numbers = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, 1):
                if keyword.lower() in line.lower():
                    line_numbers.append(i)
        return line_numbers
    except FileNotFoundError:
        return []
print(find_keyword_lines("input.txt", "python"))