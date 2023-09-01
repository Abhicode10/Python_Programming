print("1. celsium to fahrenheit")
print(("2,fahrenhieit to celsium"))

choice=int(input("Enter your choice:"))
if choice==1:
    c=float(input("Enter temprature in celsium:"))
    f=(c*9/5)+32
    print("Temprature in fahrenahite:", f)
elif choice==2:
    f=float(input("Enter temprature in fahrenahite:"))
    c=5*(f-32)/9
    print("Temprature in celsium:", c)
else:
    print("Invalid choice")


