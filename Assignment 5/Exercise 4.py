import re


def redact_phone_numbers(text):
    """
    Replace any sequence of 10 digits or numbers starting with '+84'
    with the string '[REDACTED]'.
    """
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, "[REDACTED]", text)


def main():
    text = input("Enter text: ").strip()
    result = redact_phone_numbers(text)

    print("After redaction:")
    print(result)


if __name__ == "__main__":
    main()