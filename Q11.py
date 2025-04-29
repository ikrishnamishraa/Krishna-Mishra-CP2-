print("Name: Krishna Mishra ")
print("Roll No: 24BEE109")
x_c = float(input("Enter the x-coordinate of the center: "))
y_c = float(input("Enter the y-coordinate of the center: "))
r = float(input("Enter the radius of the circle: "))
x_p = float(input("Enter the x-coordinate of the point: "))
y_p = float(input("Enter the y-coordinate of the point: "))
distance_squared = (x_p - x_c) ** 2 + (y_p - y_c) ** 2
radius_squared = r ** 2
if distance_squared < radius_squared:
print("The point is inside the circle.")
elif distance_squared == radius_squared:
print("The point is on the circle.")
else:
print("The point is outside the circle.")
