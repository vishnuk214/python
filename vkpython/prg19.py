a=int(input("Enter first numbers :"))
b=int(input("Enter second number :"))
while b:
  a,b=b,a%b
print("GCD=",a)
