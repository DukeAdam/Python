# Alice’s public key is (24852977, 2744, 8414508). You eavesdrop on the line and
# observe Bob send her the cipher (15268076, 743675). Extract the message by any
# means.

import sys
sys.setrecursionlimit(5000)

# Use for final deployment to Hackerrank
# pubKey = input("Please enter public string: ")
# cipher = input("Please enter cipher: ")

# Use for during testing to avoid inputting data every time
f = open("Test2.txt", "r")
pubKey = f.readline()
cipher = f.readline()
f.close()

# Use to split the input data
mod, base, output = pubKey.split(',',)
c1, c2 = cipher.split(',',)

# Use to remove brackets from input + convert to numbers
mod = int(mod.replace('(', ''))
base = int(base)
output = int(output.replace(')', ''))
c1 = int(c1.replace('(', ''))
c2 = int(c2.replace(')', ''))
final_pow = 0


# Brute force approach to find power
current = base
finalX = 0
for x in range(2, mod):
    # print(x)
    current *= base
    current %= mod
    if current == output:
        #print(x)
        finalX = x
        break

working = (c1 ** (mod - 1 - finalX)) % mod
finalVal = (working * c2) % mod
print(finalVal)
