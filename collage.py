Grade A: Percentage >= 80 
Grade B: Percentage >= 70 and <80
Grade C: Percentage >= 60 and <70
Grade D: Percentage >= 40 and <60
Fail: Percentage <40


# i had taken random subject names you can change them or write 'subject 1' and like that

a=float(input("enter your marks of economics :"))

b=float(input("enter your marks of history :"))

c=float(input("enter your marks of civics :"))

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



