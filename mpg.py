"""
Name: Christopher Y Sanchez
Course Name: ENTD200 B002 SUMMER2020
Instructors Name: Joseph Kivacic
Week 6
Date Completed: Sept 12, 2020
"""


def milespergallon(Mileage, Gas):
	return Mileage / Gas

process = 1
yes = "y"
no = "n"

while (process == 1) :
    Gas_Used = int(input("Enter gas used here (in gallons): "))
    Miles_Driven = int(input("Enter miles driven here: "))
    MPG = milespergallon(float(Miles_Driven),float(Gas_Used))
    print("Gas amount used: ", Gas_Used, "Gallons")
    print("Miles driven: ", Miles_Driven, "Miles")
    print("Total MPG during your trip: ", MPG, "MPG")
    choice = input("Would you like to calculate your MPG again? (y/n) : ")
    
    if (choice == "n") :
        print("Thank you for using our application.")
        break


##set process or any value at one to start a loop and maintain it. 
##Use if to set a choice with the value you had set at 1 to start the loop.
##If you set the value of == 1 into +=1 means each attempt increases the amoun
##of chances  you use.
##Set the value for action behind the choice option in the if.
##WHile keeps the loop going in sequences as long as value is met. 
##For keeps loop as long as you have not exhausted given attempts and 
##reached == 0.