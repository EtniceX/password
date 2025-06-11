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

passi = password(length)

print('Password: ', passi)

manager = passi + " "

file = open("manager.txt", "a")
file.write(manager)
file.close()
    
input('Press Enter')
