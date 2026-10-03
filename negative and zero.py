positive_number=0
negative_number=0
def positive(*numbers):
    
        global positive_number
        for num in numbers:
         if num >0:
             
             positive_number = positive_number+1

def negative(*numbers):
    
        global negative_number
        for num in numbers:
         if num<0:
            
            negative_number=negative_number+1

positive(12, -5, 0, 18, -2, 25)
negative(12, -5, 0, 18, -2, 25)
print("number of postive number:",positive_number)
print("number of negative numbre:",negative_number)

