def ispalindrome(s):
     if s.upper() == s.upper()[::-1]:
         return True


print("Write the word to check its a Palindrome")
s = input(">: ")
answer = ispalindrome(s)

if answer:
    print("Yes,It's a Palindrome")
else:
    print("No,It's not a Palindrome")
