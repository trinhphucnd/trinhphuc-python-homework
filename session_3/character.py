from random import choice , randrange

list = ("orange","apple", "watermelon")
word = choice(list)
correct = word
jumble = ""
while word:
    position = randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Question :", jumble)
guess = input("Your answer: ")
while guess != correct:
    print(":((( no")
    guess = input("Your answer: ")
if guess == correct:
    print("Oh Yeah")
