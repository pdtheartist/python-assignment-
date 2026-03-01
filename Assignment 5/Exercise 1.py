import re


def is_valid_course_code(code):
    """
    Check whether a course code is valid.
    A valid code consists of 2–3 uppercase letters followed by 3 digits.
    Example: TECO01, AU006
    """
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.fullmatch(pattern, code))


def main():
    code = input("Enter a course code: ").strip()

    if is_valid_course_code(code):
        print("Valid course code")
    else:
        print("Invalid course code")


if __name__ == "__main__":
    main()