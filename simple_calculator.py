def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

print(""" 
1.Addition
2.Subtraction
3.Multiplication
4.Division
""")

choice = int(input("Enter Your Choice>: "))
a = int(input("Enter Number 1>: "))
b = int(input("Enter Number 2>: "))

if choice == 1:
    print("The answer is: " + str(add(a, b)))
elif choice == 2:
    print("The answer is: " + str(sub(a, b)))
elif choice == 3:
    print("The answer is: " + str(multi(a, b)))
elif choice == 4:
    print("The answer is: " + str(div(a, b)))
else:
    print("!!Enter the correct choice!!")