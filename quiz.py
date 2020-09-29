import time

score = 0

name = input('Enter Your name: ')
time.sleep(0)

print('What is the speed of Rocket\nA - 7.9 kilometer/second\nB - 5 kilometer/second\nC - 10 kilometer/second')
choice = input('>> ')
if choice == 'A':
    score += 1
else:
    score += 0

print('select the even number (2,7,5)\nA - 7\nB - 2\nC - 5')
choice = input('>> ')
if choice == 'B':
    score += 1
else:
    score += 0

print(f'{name}, you have scored {score} out of 2')
