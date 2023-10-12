import random

lower = "abcdefghijklmnñopkrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "_:;=)(/&%$·"

string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string, length))

print('Password: '+password)