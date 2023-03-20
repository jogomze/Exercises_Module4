# 1. What is a variable?
#  A variable is a named reference to a value that can be changed during the execution of a program.

# 2. What is a constant?
# In Python, there is no built-in support for constants, but programmers can define constants by convention. A constant is a variable whose value is not intended to be changed during the execution of a program. 

# 3. Can a variable be changed once assigned?
# Yes, a variable can be changed once it has been assigned a value

# 4. Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the amount by which to count: "))

for i in range(start, end+1, step):
    print(i)

# 5. Create a program that gets a message from the user and then prints it out backwards.
message = input("Enter a message: ")
reversed_message = ""

for i in range(len(message)-1, -1, -1):
    reversed_message += message[i]

print("Your message reversed is:", reversed_message)


# 6. Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.

import random

# List of words for the computer to choose from
word_list = ["python", "java", "ruby", "csharp", "javascript", "html", "css", "php"]

# Pick a random word from the list
word = random.choice(word_list)

# Tell the player how many letters are in the word
print("The word has", len(word), "letters.")

# Initialize a list to keep track of the letters the player has guessed
guesses = []

# Allow the player to ask if a letter is in the word five times
for i in range(5):
    letter = input("Guess a letter of the random world I'm thinking of: ")
    if letter in guesses:
        print("You already guessed that letter. Try again.")
    else:
        guesses.append(letter)
        if letter in word:
            print("Yes, the letter is in the word.")
        else:
            print("No, the letter is not in the word.")

# Ask the player to guess the word
guess = input("You have 5 guesses to guess the word. What is your guess? ")

# Check if the player's guess is correct
if guess == word:
    print("Congratulations, you guessed the word!")
else:
    print("Sorry, the word was", word)


