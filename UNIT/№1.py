def is_palindrome(text):
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

test_cases = [
    "мадам",
    "шалаш",
    "компьютер",
    "заказ",
    "лодка",
    "топот"
]

for text in test_cases:
    if is_palindrome(text):
        print(f'"{text}" -> YES')
    else:
        print(f'"{text}" -> NO')
