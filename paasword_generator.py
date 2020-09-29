import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
             'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '*']

combined_characters = digits + lowercase + uppercase + symbols

count = input("No.of Password to generate: ")
count = int(count)

length = input("Password length: ")
length = int(length)

for p in range(count):
    password = ''
    for c in range(length):
        password += random.choice(combined_characters)
    print(password)