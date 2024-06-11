import re

def remove_punctuation_and_check(text):
    text_without_punctuation = re.sub(r'[^\w\s]', ' ', text)
    if text != text_without_punctuation:
        return "YES"
    else:
        return "NO"

test_text_correct = "Это, пример! текста, на русском языке."

test_text_incorrect = "Это пример текста на русском языке"

result_correct = remove_punctuation_and_check(test_text_correct)
print(f"Проверка текста: '{test_text_correct}', Результат: {result_correct}")

result_incorrect = remove_punctuation_and_check(test_text_incorrect)
print(f"Проверка текста: '{test_text_incorrect}', Результат: {result_incorrect}")





