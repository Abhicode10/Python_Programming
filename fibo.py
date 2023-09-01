def fabonacci(num):
   if num <= 1:
       return num
   else:
       return(fabonacci(num-1) +fabonacci(num-2))
n = int(input("Enter the number n term: "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fabonacci(i))




