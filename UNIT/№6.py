import re

def remove_punctuation_and_check(text):
    text_without_punctuation = re.sub(r'[^\w\s]', ' ', text)
    
    if text != text_without_punctuation:
        return text_without_punctuation, "YES"
    else:
        return text_without_punctuation, "NO"

input_text = input("Введите строку для проверки: ")

result_text, result = remove_punctuation_and_check(input_text)
print(f"Измененный текст: '{result_text}', Результат проверки: {result}")





