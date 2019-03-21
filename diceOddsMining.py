# Program to understand how Bitcoin mining works
# Represented by rolling a dice, if at the same time that a 6 is rolled,
# at 600 seconds (average time between a coin being mined) then for all
# those occasions where a Bitcoin block happens to be mined during your
# rollings, how many rolls on average are needed before getting a 6?

from random import randint
max_num = 1000000
num_occurences = 0
bitcoin_found = False
running_count = 0
last_six = 0

for x in range(max_num):
    rand_num = randint(1, 6)

    if x % 600 == 0:
        bitcoin_found = True

    if (rand_num == 6) and bitcoin_found:
        running_count += (x - last_six)
        num_occurences += 1
        bitcoin_found = False

    elif rand_num == 6:
        last_six = x

print(running_count / num_occurences)

