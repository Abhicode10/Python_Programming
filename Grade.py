total=int(input("Enter the maximum mark of a subject: "))

sub1=int(input("Enter marks of the first subject: "))

sub2=int(input("Enter marks of the second subject: "))

sub3=int(input("Enter marks of the third subject: "))

sub4=int(input("Enter marks of the fourth subject: "))

sub5=int(input("Enter marks of the fifth subject: "))

average=(sub1+sub2+sub3+sub4+sub5)/5 
print("Average is ",average)
percentage=(average/total)*100
print("According to the percentage, ")
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80 and percentage < 90:
    print("Grade: B")
elif percentage >= 70 and percentage < 80:
    print("Grade: C")
elif percentage >= 60 and percentage < 70:
    print("Grade: D")
else:
    print("Grade: E")