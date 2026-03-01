import re


def is_valid_hex_color(color):
    """
    Check whether a string is a valid hexadecimal color.
    A valid hex color starts with '#' followed by exactly 6 hexadecimal characters.
    """
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.fullmatch(pattern, color))


def main():
    color = input("Enter a hex color: ").strip()

    if is_valid_hex_color(color):
        print("Valid hex color")
    else:
        print("Invalid hex color")


if __name__ == "__main__":
    main()