import random
import string
def password(strength):
    password = [random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(1,15)]
    password = "".join(password)
    return password

print(password(5))