import random
import string

password_len = 8 

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
password = ''.join(random.choice(chars) for _ in range(password_len))

print(f"Generated Password: {password}")
