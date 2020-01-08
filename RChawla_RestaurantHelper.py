print ('Welcome to Restaurant Helper!')


#get bill amount
bill = raw_input("Enter total bill: ")

#convert into float
bill = float(bill)

#add Wisconsin State Tax (5%)
bill = bill*1.05

#get tip percentage
tip = raw_input("Enter tip percentage: ")

#convert to float
tip = float(tip)

#change to a decimal
tip = tip/100

#get number of people
people = raw_input("Enter number of people to split between: ")

#convert to int
people = int(people)

#function to calculate bill
def calculateTotal(bill,tip):

    total = (bill + (bill*tip))/(people) 
    return total


#return bill
print ('Each person will pay: ' + str(calculateTotal(bill,tip)))


