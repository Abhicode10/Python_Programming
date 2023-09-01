def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1

    else:
        return (n*factorial(n-1))
n=int(input("Enter the number:"))
result=factorial(n)
print("The factorial of",n,"is",result)