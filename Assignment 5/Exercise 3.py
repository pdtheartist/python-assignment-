import re


def sum_of_numbers_in_text(text):
    """
    Find all integer numbers in a given text and return their sum.
    """
    numbers = re.findall(r'\d+', text)
    integers = [int(num) for num in numbers]
    return sum(integers)


def main():
    paragraph = input("Enter a paragraph: ").strip()
    result = sum_of_numbers_in_text(paragraph)

    print("Sum of numbers:", result)


if __name__ == "__main__":
    main()