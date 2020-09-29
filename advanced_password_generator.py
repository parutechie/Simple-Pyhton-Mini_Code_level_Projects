import random

#getting inputs from the user
user_input = input("Enter the letter's separated by space: ")
userlist = user_input.split()

#number of password to generated
count = input("No.of Password to generate: ")
count = int(count)

#length of the password
length = input("Password length: ")
length = int(length)

for p in range(count):
    password = ''
    for c in range(length):
        password += random.choice(userlist)
    print(password)
    password += '\n'

    #creating a txt file to save the generated password
    with open('output.tx', "a")as file:
        file.write(password)
        file.close()
