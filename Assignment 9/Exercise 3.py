def calculate_average_score(file_name):
    total_score = 0
    count = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if ',' in line:
                    # Split name and score
                    parts = line.split(',')
                    # Get the score (part after the comma) and convert to float
                    score = float(parts[1].strip())
                    total_score += score
                    count += 1
        return total_score / count if count > 0 else 0
    except Exception:
        return 0
print(calculate_average_score("input.txt"))