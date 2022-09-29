#Initiates Variables
average = 0
total = 0
howManyEntered = 0
howMany = int(input("How many test scores would you like to enter? "))

#Ask user for input
while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total = testScore + total
    howManyEntered += 1
    
#Calculate the Average
    if howManyEntered == howMany:
        average = total / howMany
        print("The average for the test scores you entered is: ", average)
    
