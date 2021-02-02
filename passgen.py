# Program Version 1.0.0
# Password Generator


import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "0123456789"

symbols = "!@#$%^&*()_+-=,./<>?;':[]{}`~"

length = 16

all = lower + upper + number + symbols

password = "".join(random.sample(all,length))

print("Password is: ", password)
