print("Name: Krishna Mishra ")
print("Roll No: 24BEE109")
x1 = int(input("Enter x1 for point 1: "))
x2 = int(input("Enter x2 for point 2: "))
x3 = int(input("Enter x3 for point 3: "))
area = x1 * (x2 - x3) + x2 * (x3 - x1) + x3 * (x1 - x2)
if (area == 0):
print("The points lie on same line")
else:
print("The points don't lie on same line")
