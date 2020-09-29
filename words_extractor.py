#create a file named'input.txt' to extract the word

extractor = input("Enter the letter to extract: ")
lists = []

with open('input.txt', 'r+') as f:
    for word in f:
        temp = word.split()
    for letter in temp:
        if letter[0].lower() == extractor.lower():
            lists.append(letter)

print(f"The extracted words from given letter '{extractor}' are : ", str(lists))
