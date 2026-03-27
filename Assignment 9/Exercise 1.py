def count_lines(file_name):
    count = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    count += 1
        return count
    except FileNotFoundError:
        return 0
print(count_lines("input.txt"))