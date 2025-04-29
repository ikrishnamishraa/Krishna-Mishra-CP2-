print("Name: Krishna Mishra ")
print("Roll No: 24BEE109")
list = [("24BEE109","Hello",18),("24BEE110","Hi",20),("24BEE112","Bye",19)]
rollnum =[]
age=[]
name=[]
for i in list:
    rollnum.append(i[0])
    age.append(i[2])
    name.append(i[1])
print(f"Roll number : {rollnum}")
print(f"Name : {name}")
print(f"Age:{age}")
