import random
import string


def random_email():
    username_letter = ''.join(random.choice(string.ascii_letters.lower()) for _ in range(5))
    username_digit = ''.join(random.choice(string.digits) for _ in range(3))
    domain = random.choice(["gmail", "yahoo", "outlook"])
    tld = random.choice(["com", "net", "bd", "edu"])

    email = f"{username_letter}{username_digit}@{domain}.{tld}"
    return email


print(random_email())


def random_password():
    password_letter = ''.join(random.choice(string.ascii_letters.lower() + string.ascii_letters.upper()) for _ in range(5))
    password_digit = ''.join(random.choice(string.digits) for _ in range(3))
    password_special_characters = ''.join(random.choice(string.punctuation) for _ in range(2))

    password = f"{password_letter}{password_digit}{password_special_characters}"
    return password


print(random_password())
