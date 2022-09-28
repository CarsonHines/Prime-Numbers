
userNumber = int(input("Enter an integer greater than 1: "))
numList = []
factors = []
primeList = []
def comp():
    print(userNumber, "= Composite")

def prim():
    print(userNumber, "= Prime")

for x in range(1, userNumber + 1):
    numList.append(int(x))

for x in numList:
    if not userNumber % x:
        factors.append(int(x))

if len(factors) > 2:
    comp()

elif len(factors) <= 2:
    prim()

else:
    print("Your integer is less than 1. Try again. ")

#Counts all number up to the user's input
for x in range(2, userNumber + 1):
        #Uses each number up to the user's input as the max number in this loop
        for i in range(2, x):
            #If the remainder of all iterations of userNumber divided by all iterations of X is equal to 0.
            if (x % i) == 0:
                break
        else:
            primeList.append(x)

print("All prime numbers up to", userNumber, "-", primeList)
