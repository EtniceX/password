import random
import string

length = int(input('Password length: '))

def password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    all_chars = lowercase + uppercase + digits
    
    password = "".join(random.choice(all_chars)for i in range(length))
    return password

print('Password: ', password(length))


    
input('Press Enter')
