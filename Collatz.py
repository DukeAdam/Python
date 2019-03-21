# Program to test the Collatz theory that every number which runs through the Collatz sequence end up at 1
# Programming constraint is that the sequence must run through a particular number, in this case my student number

maxCount = [1]
maxCurrent = [1]
def collatzTestToNum(test):
    found = False
    while found:
        if test % 2 == 0:
            test = test / 2
        else:
            test *= 3
            test += 1
        if test == 1:
            break
        if test == 17718781:
            found = True
    return found

def collatzTestToOne(test, maxCount, maxCurrent, outerLim):
    count = 0
    current = test
    cur = test
    while test != 1:
        if test % 2 == 0:
            test = test / 2
        else:
            test *= 3
            test += 1
        count += 1
    if count > maxCount[0]:
        maxCount[0] = count
        maxCurrent[0] = current
        print("New max iterations is: " + str(maxCount[0])+ "\tat number: " + str(maxCurrent[0]))
    if cur == outerLim - 1:
        print("=========END=========")

innerLim = 1
outerLim = 100000
for x in range(innerLim, outerLim):
    collatzTestToOne(x, maxCount, maxCurrent, outerLim)