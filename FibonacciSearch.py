# Begin by asking a user for a number
print("How many numbers do you want to check?")
amountNum = int(input())
numOn = 0
numList = []
while numOn < amountNum:
    print("Enter a number")
    userNum = int(input())
    numList.append(userNum)
    numOn += 1


def fib_find(num):
    # Check if the number is equal to 1 or 0, if so then return true
    if num == 0 or num == 1:
        return True
    else:
        firstTerm = 0
        secondTerm = 1
        running = True
        while running:
            # Performs the action of finding the next term
            addedTerms = firstTerm + secondTerm
            # Checks if the new term is the same as the user's number. If so, true is returned.
            if addedTerms == num:
                return True
            # Checks if the new term already surpassed the user's number. If so, sets running as false.
            elif addedTerms > num:
                running = False
            # Continues the process of setting new terms
            else:
                firstTerm = secondTerm
                secondTerm = addedTerms
        # Returns false at the very end
        return False


# Goes through each value the user enters
for num in numList:
    # Takes the current number and finds if it is in the fibonacci sequence
    currentNum = fib_find(num)
    # Prints out the number and whether or not it was in the fibonacci sequence
    print("The number is: " + str(num) + ". Is it in the fibonacci sequence? " + str(currentNum))
