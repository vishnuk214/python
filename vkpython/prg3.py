n=int(input("Enter number :"))
numbers=[]
for i in range(n):
    x=int(input("Enter number :"))
    numbers.append(x)
squares=[x*x for x in numbers]
print("squares:",squares)
