import string
from random import choices
m=int(input('tedad char='))

def create_password(length=m , upper=False, lower=False, digit=False,pun=False):
    first_char_pool=[]#first character of password
    last_char_pool=[]#last character of password
    pool=[]#password characters -(first character and last character)
    if upper:
        first_char_pool+=string.ascii_uppercase
        pool += string.ascii_uppercase
       # pool[0]+=string.ascii_uppercase
        last_char_pool+=string.ascii_uppercase
    if lower:
        first_char_pool+=string.ascii_lowercase
        pool += string.ascii_lowercase
       # pool[0]+=string.ascii_lowercase
        last_char_pool+=string.ascii_lowercase
    if digit:
        first_char_pool+=string.ascii_lowercase
        pool += string.digits
        #pool[0]+=string.digits
    if pun:
        pool+= string.punctuation  
    if pool==[]:
        first_char_pool+=string.ascii_letters
        pool = string.ascii_letters 
        last_char_pool+=string.ascii_lowercase
         
    first= choices(first_char_pool , k=1)
    second=choices(pool , k=m)
    last=choices(last_char_pool, k=1)
    return ''.join(second)
if __name__ == '__main__':
   #print(create_password(upper=True))
   #print(create_password(lower=True))
   print(create_password(upper=True ,lower=True , digit=True , pun=True))
   
   
 
 
   