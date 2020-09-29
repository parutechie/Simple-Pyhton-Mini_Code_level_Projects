import random

print("""
Guess The Number
Guess the nuber from 1 to 10
""")
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    elif guess < secret_number:
        print("Your guess was too low: Guess a number higher than",guess)
    else:
        print("Your guess was too high: Guess a number lower than",guess)
else:
        print(f"Sorry wrong guess!! The Number is {secret_number}")