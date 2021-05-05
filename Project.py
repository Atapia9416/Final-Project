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
    A=float(input1)
    r=float(input2)
    n=float(input3)
    i=r/1200
    emi=(A*i)/(1-(1+i)**(-12*n))
    print("Monthly Payment:",'$'+str('%.2f'%emi))
    print ("Payment #".ljust(20), "Payment Amount".ljust(20), "Interest Payed".ljust(20), "Ending Balance".ljust(20)) 
    count = 0

    while (count < n*12):
        count += 1
        print(str(count).ljust(20))
Emi()
