import re

def validate_phone_number(phone_number):
    pattern = r'^(\+7|8)( ?\(?(\d{3})\)? ?)?(\d{3}[- ]?\d{2}[- ]?\d{2})$'
    
    match = re.match(pattern, phone_number)
    
    if match:
        return "YES"
    else:
        return "NO"

phone_number = input("Введите номер телефона: ")

print(validate_phone_number(phone_number))
