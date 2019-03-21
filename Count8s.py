# Read in a number, count the number of 8's in it recursively.
# If there are two 8's touching, this counts as an extra 8

def count8(data, count):
    if data <= 0: #base case
        return count
    else:
        if data % 100 == 88: #check if there are 2 8's touching
            count+=2
            data//=10 # divide to a decimal value, stop it going to min value
        elif data % 10 == 8:
            count +=1
            data//=10
        else: data//=10
        return count8(data, count)

read = int(input())
counter = 0
counter = count8(read, counter)
print(counter)

# Test val: 8832858822
# Results in 7, 5 8's in sequence plus 2 double occurrences