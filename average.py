average = 0
total = 0
howmanyentered = 0

howmany = int(input("how many test scores would you like to average?"))
testscore = int(input("enter test score"))
total = total + testscore
howmanyentered = howmanyentered + 1

while howmanyentered != howmany:
    testscore = int(input("enter test score"))
    total = total + testscore
    howmanyentered = howmanyentered + 1


    average = total / howmany
    print ("the average of the test scores you entered is:")
    print (average)
