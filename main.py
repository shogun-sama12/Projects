import random 
import string
letters = string.ascii_letters
digts=string.digits
symbols= string.punctuation
all_symbol=letters+digts+symbols
def password_generator(n,quantity):
    p=[]
    if n<8:
        return 'No less than 8 characters'
    for _ in range(quantity):
        p.append(''.join([random.choice(all_symbol) for _ in range(n)]))
    return p
n = int(input('password length:'))
quantity=int(input('quantity:'))
print(password_generator(n,quantity))