import random
import string
def password_generator():
    print("Welcome to our Random Password Generator")
    lenght = int(input("Enter the Lenght of the Password you want to enter: "))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    sysbolsD = string.punctuation
    combine = lowerD+upperD+digitD+sysbolsD
    x = random.sample(combine,lenght)
    password = "".join(x)
    print(password)
password_generator()