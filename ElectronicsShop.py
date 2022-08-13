

user_input = int(input("enter your choice from 1 to 4: "))
if user_input == 1:
    num1 = int(input("enter a number whose factorial you want to find: "))
    fact = 1
    while num1>0:
        fact = fact * num1
        num1 = num1 - 1
    print(fact)

elif user_input == 2:
    num2 = int(input("enter a number you wanna find whether its armstrong or not: "))
    temp = num2
    sum = 0
    while num2 > 0:
        sepdigi = num2%10
        sum = sum + (sepdigi*sepdigi*sepdigi)
        num2 = num2//10
    if sum == temp:
        print("armstrong number")
    else:
        print("not armstrong number")

elif user_input == 3:
    num3  = int(input("enter a number you wanna find whether its strong or not: "))
    fact = 1
    temp = num3
    sum = 0
    while num3>0:
        sepdigi = num3%10
        fact = 1
        while sepdigi>0:
            fact = fact * sepdigi
            sepdigi = sepdigi - 1
        sum = sum + fact
        num3 = num3 // 10
    if sum == temp:
        print("its a strong number")
    else:
        print("not a strong number")
elif user_input == 4:
    num4 = int(input("enter a number you wanna find whether its a perfect number or not: "))
    temp = num4
    sum = 0
    for i in range(1, num4 - 1):
        if num4 % i == 0:
            sum = sum + i
    if sum == temp:
        print("perfect number")
    else:
        print("not perfect number")

else:
    print("enter correct input")