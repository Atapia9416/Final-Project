"""
The code will calcualte and create an amortization table for a simple loan by taking in the inputs of Loan amount, interest rate, loan period (years) and 
output how much you're paying towards interest rates and principle for each of your payements (monthly). You will have a choice
between EMI and Simple Interest to see how much interest you are paying off and how much balance you have left to pay.

"""




def SI():     #Function that generates table for Simple Interest loans
     input1 = input("Enter amount of loan: ") # Principle of Loan
     input2= input("Enter interest rate: ")  #Interest rate of loan
     input3 = input("Enter number of years: ") #Years of loan
     A=float(input1) # Principle
     r=float(input2) # rate
     n=float(input3) # years
     SI = A * (1+ (r/100)*n) #total payed after interest
     cb = SI #closing balance
     mr = float((SI - A)/(n*12)) #interest per month
     mp = SI/(n*12)  #monthly payment
     print("Monthly Payment:", '$'+str('%.2f\n'%mp))   #Prints out Monthly payment 
     count = 0    #Starts counter


     print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Principle Payed".ljust(20), "Ending Balance\n".ljust(20)) 
     while (count < n*12):
         count += 1
         pp = mp
         cb = cb - pp
         print(str(count).ljust(20), str('%.2f'%mp).ljust(20), str('%.2f'%mr).ljust(20), str('%.2f'%pp).ljust(20), str('%.2f'%cb).ljust(20)) 



def Emi():
    input1 = input("Enter amount of loan: ")
    input2= input("Enter interest rate: ") 
    input3 = input("Enter number of years: ") 
    A=float(input1) # Principle
    r=float(input2) # rate
    n=float(input3) # years
    mr=float(r/12)  #monthly rate
    cb = A #closing balance
    i=r/1200       #i for equation to be simplifed
    emi=(A*i)/(1-(1+i)**(-12*n))      #Calculates monthly payment 
    print("Monthly Payment:",'$'+str('%.2f\n'%emi))   #Prints out monthly payment
    print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Principle Payed".ljust(20), "Ending Balance\n".ljust(20)) #Table heading
    count = 0         #^^^^ headers for data rows
    print(str(cb).rjust(91))


    while (count < n*12):  #Stops generating rows once months count is hit >>>>(n) monthis times 12
        count += 1         #Counts each row generated on table
        ip = ((mr/100)*cb) #Monthly interest payed
        emi = emi
        pp = emi - ip    #Principle paymant is monthly payment minus interest payed
        cb = cb - pp      #Subtracts principle payed from the balance
        print(str(count).ljust(20), str('%.2f'%emi).ljust(20), str('%.2f'%ip).ljust(20), str('%.2f'%pp).ljust(20), str('%.2f'%cb).ljust(20)) 
        #^^^^ prints out the row of data
Method = ""
Method = input("What kind of interest is the loan?\n Would you like EMI (Equated monthly installment) or SI (Simple Interest)?\n")
if Method == "EMI":                         # Determines which function to run
    print("You have Chosen EMI\n")
    Emi()
elif Method == "SI":
    print("You have chosen Simple Interest\n")
    SI()
else:
    print("Not Available")