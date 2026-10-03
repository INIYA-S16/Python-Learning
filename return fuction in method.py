positive_number=0
negative_number=0
zero=0
def number(*number):
    for num in number:
        global positive_number
        global negative_number
        global zero
        
        if num >0:
            positive_number=positive_number+1
        elif num < 0:
            negative_number=negative_number+1
        elif num==0:
            zero=zero+1
    return positive_number,negative_number,zero
result=number(12, -5, 0, 18, -2, 25, 0)
print(result)

