a=float(input("enter your marks of Maths :"))
b=float(input("enter your marks of Computer :"))

c=float(input("enter your marks of English :"))

s=(a+b+c)/300*100

if s>=80:

   print("GRADE A")

elif s>= 70 and s<80:

   print("GRADE B")

elif s>=60 and s<70:

   print("GRADE C")

elif s>=40 and s<60:

   print("GRADE B")

elif s<40:

   print("FAIL")
