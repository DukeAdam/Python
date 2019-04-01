# Adam Duke - 17718781
# Create a game of hangman based on all words in the dictionary

from random import randint

f = open("Dictionary.txt", "r")
dictionary = []
for x in f:
    dictionary.append(x)  # populate the dictionary array with values from the text file
f.close()

# word_pos = int(input("Please enter a number: "))  # use to test a particular word
word_pos = randint(0, 216555)  # use for actual game-play with a random number
word = dictionary[word_pos - 1]  # find the random word in the array
word_len = int(len(word) - 1)  # word length
num_lives = 3
guess_word = []
correct_letters = 0
brk = False

print(word)

for x in range(0, word_len):
    guess_word.append("_")

while True:
    char = input("\nPlease guess a letter: ")
    if len(char) > 1:  # check to prevent muliple characters
        print("Please input 1 character at a time")
        continue
    lttr_change = False
    for y in range(0, word_len):
        if char == word[y]:  # deals with multiple identical letters by imputting them all
            guess_word[y] = word[y]
            correct_letters += 1  # keep a running count of correct letters, use to know when word is complete
            lttr_change = True
            print("Correct guess :)")
        if correct_letters == word_len:
            print("YOU WIN!!!")
            brk = True  # need to execute a double break 
            break
        if y == word_len - 1 and lttr_change is False:
            num_lives -= 1
            print("Wrong letter, ", str(num_lives), " lives left", end = "")
            if num_lives == 0:
                print(" - You lose")
                brk = True
                break
    print("\n", guess_word, end="\n")
    if brk:
        break
