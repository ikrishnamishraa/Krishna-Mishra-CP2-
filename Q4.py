print("Name: Krishna Mishra ")
print("Roll No: 24BEE109")
'''def perfect():
    l=[]
  
    c=0
    d=0
    
    n = int(input("Enter the range"))
    for i in range (n):
        l.append((int(input("Enter the values of list"))))
       

    
    for a in l:
        j=a
        sum=0
       
        
        while a>0:
            sum+=a%10
            a//=10
        if j==sum:
            c+=1
        else:
            d+=1
    print(f"The number of perfect numbers is {c}")
    print(f"the number of non perfect numbers is {d}")
perfect()'''
def perfect():
    l = []  
    c = 0  
    d = 0  
    
    n = int(input("Enter the range: "))
    
   
    for i in range(n):
        l.append(int(input(f"Enter the value of the list at index {i+1}: ")))
  
    for a in l:
        original_a = a  
        sum_digits = 0  
        
        
        while a > 0:
            sum_digits += a % 10
            a //= 10
        
      
        if original_a == sum_digits:
            c += 1
        else:
            d += 1
    
  
    print(f"The number of digit-sum-perfect numbers is {c}")
    print(f"The number of non-digit-sum-perfect numbers is {d}")


perfect()
