# GUVI - Task 3 - Q.No 1 - Guess the number

import random

number = (random.randint(1,500))
attempts = 0

print("Guess the number between 1 and 500 !!!!!!")

while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
                print("Number Too High. Try again")
                print()
        elif guess < number:
                print("Number Too Low. Try again")
                print()
        else:
                print(f"Congratulations!!!, You guessed the correct number in {attempts} attempts")
                break


# GUVI - Task 3 - Q.No 2 - Word Scramble

import random
print('Welcome to Unscrambler')
print('Unscramble the Following Words..!!!!')
input('Press Enter to Start the Game...! ')
print()
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
newword = ''
count = 0

for word in range (len(words)):
        scrambled = "".join(random.sample(words[word], len(words[word])))
        print(f"Unscramble this: {scrambled}")
        guess = input('Write here: ')
        if guess == words[word]:
                print('Correct...!!!')
                print()
                count += 1
        else:
                print('Wrong...!!!! Try again')
                print()

print(f'You scored {count}!!')
print()
if count <= len(words)/2:
        print('Good try... You are Terrible...!!!')
else:
        print('Wonderful... You are Amazing... A Good Gamer')
print()