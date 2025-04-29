print("Name: Krishna Mishra")
print("Roll No: 24BEE109")
no1 = int(input("Enter Number 1: "))
no2 = int(input("Enter Number 2: "))
no3 = int(input("Enter Number 3: "))
if no1 > no2:
if no1 > no3:
largest = no1
else:
largest = no3
if no2 > no3:
largest = no2
else:
largest = no3
if no1 < no2:
if no1 < no3:
smallest = no1
else:
smallest = no3
if no2 < no3:
smallest = no2
else:
smallest = no3
print("The Largest Number Is:", largest)
print("The Smallest Number Is:", smallest)
