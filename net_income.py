s=int(input("enter the annual income:"))
a=float(input("enter the deduction1:"))
b=float(input("enter the deduction2:"))
c=float(input("enter the deduction3:"))
n=int(input("no.of weeks:"))
k=n*s*(1-((a+b+c)/100))
print("%.2f" %k)