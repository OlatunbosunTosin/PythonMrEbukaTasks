x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
if x < 0 and y < 0:
    print("Q3")
if x > 0 and y < 0:
    print("Q4")
if x == 0 and y == 0:
    print("Origin")
if x != 0 and y == 0:
    print("X-axis")
if x == 0 and y != 0:
    print("Y-axis")
