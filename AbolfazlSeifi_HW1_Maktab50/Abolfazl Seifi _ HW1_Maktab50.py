# Compound interest Rate

p=int(input("Enter initial principal balance: "))
r=int(input("interest rate: "))
n=int(input("number of times interest applied per time period: "))
t=int(input("number of time periods elapsed: "))
A=p*(1+r/n)**(n*t)
print("\nCompound Rate is : ", A)





# Created by Abolfazl Seifi
