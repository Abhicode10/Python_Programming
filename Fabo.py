a=10;b=20;c=30
print(a);print(b);print(c)

x,y,z=10,20,30
print(x);print(y);print(z)

mylist=[10,20,30,40]
mylist.append([50,60])
print(mylist)

my_list=[10,20,30,40]
anotherlist=[80,90]
my_list.extend(anotherlist)
print(my_list)

A=20
B=7

print(A&B)

a="j"
print(a,"is of type", type(a))

z=20
print(z,bin(z))
x=7
print(x,bin(x))

mylist[3]="Abhishek"
print(mylist)

D={"n":"abhishek",90:'maths',85:'computer'}

print(D,type(D))

D={85:"Python"}
print(D,type(D))

s={1,2,3,10,20,10,20,1}
print(s,type(s))

m=eval(input("Enter number 1="))
n=eval(input("Enter number 2="))

print("Sum of two number=", m+n)


A=int(input("Enter any number:"))
if A%2==0:
    print("Even Number")
else:
    print("Odd Number")

A=int(input("Enter your percentage:"))

if[A>=80 and 100<=A]:
    print("Grade A")
elif[A>=70]:
    print("Grade B")
elif[A>=60]:
    print("Grade C")
elif[A>=35]:
    print("Grade D")
else:
    print("Fail")











