import re

def validate_phone_number(phone_number):
    pattern = r'^(\+7|8)( ?\(?(\d{3})\)? ?)?(\d{3}[- ]?\d{2}[- ]?\d{2})$'
    
    match = re.match(pattern, phone_number)
    
    if match:
        return "YES"
    else:
        return "NO"

test_cases = [
    "+7(900)1234567",
    "+7 900 1234567",
    "890012345",
    "+7 900 123456725",
    "+79901234567",
    "+45822564983",
    "8 (900) 1234567",
    "+89001234567",
    "8 900)1234567",
    "+7 900(1234567",
    "8 900 1234567",
    "аьуутеиккеиу",
]

for phone_number in test_cases:
    print(f"Номер: {phone_number}, {validate_phone_number(phone_number)}")





