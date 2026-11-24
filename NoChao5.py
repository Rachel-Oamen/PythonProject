reverse = ""

word = input("Enter a word: ")

for count in range(len(word)
    reverse = reverse + word[count]

if word.lower() == reverse.lower():
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
