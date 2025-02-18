import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_number(start, end):
    return random.randint(start, end)

def create_random_username():
    random_letters = generate_random_string(3)
    random_number = generate_random_number(10, 99)
    random_username = f'dmitry_{random_letters}_{random_number}'
    return random_username
    #Генерация email для регистрации
def create_random_email():
    random_letters = generate_random_string(4)
    random_number = generate_random_number(100, 999)
    random_email = f'sharonov_dmitry_14a_{random_letters}_{random_number}@yandex.ru'
    return random_email

    #Генерация пароля для регистрации
def create_random_password():
    random_letters = generate_random_string(3)
    random_number = generate_random_number(10, 999)
    random_password = f'asd_{random_letters}_{random_number}'
    return random_password
