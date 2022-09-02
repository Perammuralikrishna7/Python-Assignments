min=int(input("Enter value of x"))
max=int(input("Enter value of y"))

for n in range(min,max+1):
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                break
            else:
                print(n)