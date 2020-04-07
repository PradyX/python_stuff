marks = int(input("Enter Marks : "))

if marks > 100 or marks < 0:
    print("Error")
elif marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")
