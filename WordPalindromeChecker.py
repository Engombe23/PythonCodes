# Assessed task 4 - Week 4

word = input("Enter a word: ")

wordPalindrome = ""

for i in range(1, len(word) + 1):
    wordPalindrome += word[i * -1]

if word == wordPalindrome or word == wordPalindrome.capitalize() or word == wordPalindrome.upper():
    print("Word " + word + " is a palindrome")
else:
    print("Word " + word + " is not a palindrome")
 