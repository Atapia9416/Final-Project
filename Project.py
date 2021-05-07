"""
The code will calcualte and create an amortization table for a simple loan by taking in the inputs of Loan amount, interest rate, loan period (years) and 
output how much you're paying towards interest rates and principle for each of your payements (monthly).

"""
"""
prin = 0
rate = 0
years = 0

prin = int(input("What is the loan principle?:\n"))
rate = float(input("What is the interest rate? ex (5%, input 0.05):\n"))
years = int(input("How many years is the loan for?:\n"))
n = years * 12

total = prin*((1+(rate/(n)))**(n*years))
print (total)

print ("Payment #".ljust(20), "Payment Balance".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Ending Balance".ljust(20))


#while(n <= years* 12):

"""

#input("What kind of interest is the loan?\n")

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
    print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Principle Payed".ljust(20), "Ending Balance\n".ljust(20)) 
    count = 0
    print(str(cb).rjust(91))


    while (count < n*12):
        count += 1
        ip = ((mr/100)*cb) #Monthly interest payed
        emi = emi
        pp = emi - ip
        cb = cb - pp
        print(str(count).ljust(20), str('%.2f'%emi).ljust(20), str('%.2f'%ip).ljust(20), str('%.2f'%pp).ljust(20), str('%.2f'%cb).ljust(20)) 
        

Emi()