num = eval(input("Enter a number : "))
sumdig = num
length = len(str(num))
while length>1:
    num = sumdig
    sumdig = 0
    while num>0:
        rem = num%10
        sumdig+=rem
        num=num//10
    length = len(str(sumdig))
    
print("The sum is : ",sumdig)
