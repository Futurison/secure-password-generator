import random
import string
import pprint

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

password = generate_password(10)
pprint.pprint("Your secure password is: " + password)
input("Press enter to exit")
