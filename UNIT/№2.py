def is_palindrome(text):
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

user_input = input("Введите текст: ")

if is_palindrome(user_input):
    print("YES")
else:
    print("NO")
