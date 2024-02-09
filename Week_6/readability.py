from cs50 import get_string

# prompts user for a card number
text = get_string("Text: ")

# counts letters, words and sentences
letters = 0
sentences = 0
words = 1
lastChar = ""
newText = text.lower()

for char in newText:
    if ord(char) in range(ord("a"), ord("z") + 1):
        letters += 1
    if char == " ":
        words += 1
    if char in ".?!":
        if lastChar not in ".?!":
            sentences += 1
    lastChar = char

# computes Coleman-Liau index
l = letters / words * 100
s = sentences / words * 100
x = 0.0588 * l - 0.296 * s - 15.8

# prints grade
if x > 15:
    print("Grade 16+")
elif x < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(x)}")
