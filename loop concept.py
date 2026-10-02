numbers=[]
for i in range(5):
    num=int(input("Enter the number:"))
    numbers.append(num)
pos_num=0
neg_num=0
for num in numbers:
    
    if num >0:
        pos_num=pos_num+1
    elif num<0:
        neg_num=neg_num+1
    elif num==0:
        print("Zero is not valid")
else:
    print("Invalid input")

    
        