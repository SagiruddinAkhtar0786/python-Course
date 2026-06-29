"""Regular expression examples in Python."""

import re

# Example 1: Search for an email address in text

def find_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


# Example 2: Validate a simple phone number format

def is_valid_phone(phone):
    pattern = r"^\+?[0-9]{1,3}?[- ]?[0-9]{10}$"
    return re.match(pattern, phone) is not None


# Example 3: Split a sentence into words using non-word separators

def split_words(sentence):
    pattern = r"\W+"
    return [word for word in re.split(pattern, sentence) if word]


# Example 4: Replace all numbers in text with [NUMBER]

def replace_numbers(text):
    pattern = r"\d+"
    return re.sub(pattern, "[NUMBER]", text)


if __name__ == "__main__":
    sample_text = "Contact us at support@example.com or sales@example.org."
    print("Found emails:", find_email(sample_text))

    phone1 = "+919876543210"
    phone2 = "123-4567"
    print(phone1, "valid?", is_valid_phone(phone1))
    print(phone2, "valid?", is_valid_phone(phone2))

    sentence = "Hello, world! Welcome to regex 101."
    print("Split words:", split_words(sentence))

    text_with_numbers = "Order 123 from store 456."
    print("Replace numbers:", replace_numbers(text_with_numbers))
