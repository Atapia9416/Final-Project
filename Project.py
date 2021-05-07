"""
The code will calcualte and create an amortization table for a simple loan by taking in the inputs of Loan amount, interest rate, loan period (years) and 
output how much you're paying towards interest rates and principle for each of your payements (monthly).

"""
"""


"""




def SI():
     input1 = input("Enter amount of loan: ") 
     input2= input("Enter interest rate: ") 
     input3 = input("Enter number of years: ") 
     A=float(input1) # Principle
     r=float(input2) # rate
     n=float(input3) # years
     cb = A #closing balance
     SI = A*(1+(r/100)*n) #total payed after interest
     print(SI)
     mr = float(r/12) #interest per month
     mp = SI/(n*12)  #monthly payment
     print("Monthly Payment:", '$'+str('%.2f\n'%mp))
     count = 0


     print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Principle Payed".ljust(20), "Ending Balance\n".ljust(20)) 
     while (count < n*12):
         count += 1
         ip = ((mr/100)*cb) #Monthly interest payed
         pp = SI - ip
         cb = cb - pp
         print(str(count).ljust(20), str('%.2f'%mp).ljust(20), str('%.2f'%ip).ljust(20), str('%.2f'%pp).ljust(20), str('%.2f'%cb).ljust(20)) 


def Emi():
    input1 = input("Enter amount of loan: ") 
    input2= input("Enter interest rate: ") 
    input3 = input("Enter number of years: ") 
    A=float(input1) # Principle
    r=float(input2) # rate
    n=float(input3) # years
    mr=float(r/12)  #monthly rate
    cb = A #closing balance
    i=r/1200
    emi=(A*i)/(1-(1+i)**(-12*n))
    print("Monthly Payment:",'$'+str('%.2f\n'%emi))
    print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Principle Payed".ljust(20), "Ending Balance\n".ljust(20)) #Table heading
    count = 0
    print(str(cb).rjust(91))


    while (count < n*12):
        count += 1
        ip = ((mr/100)*cb) #Monthly interest payed
        emi = emi
        pp = emi - ip
        cb = cb - pp
        print(str(count).ljust(20), str('%.2f'%emi).ljust(20), str('%.2f'%ip).ljust(20), str('%.2f'%pp).ljust(20), str('%.2f'%cb).ljust(20)) 
        
Method = ""
Method = input("What kind of interest is the loan?\n Would you like EMI or SI (Simple Interest)?\n")
if Method == "EMI":
    print("You have Chosen EMI\n")
    Emi()
elif Method == "SI":
    print("You have chosen Simple Interest\n")
    SI()
else:
    print("Not Available")