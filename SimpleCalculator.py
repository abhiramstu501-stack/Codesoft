#simple calculator for two Numbers and Arithematic Operations
num1=int(input("Give value of number 1: "))
num2=int(input("Give value of number 2: "))
operator=input("Give a operator: ")
if operator=="+":
    print(f"Addition of Two numbers {num1+num2}")
elif operator=="-":
    print(f"Subtraction of Two numbers {num1-num2}")
elif operator=="*":
    print(f"Multiplication of Two numbers {num1*num2}")
elif operator=="/":
    print(f"Divison of Two numbers {num1/num2}")
elif operator=="**":
    print(f"Squaring of a Number {num1**num2}")
else:
    print("Not Valid")

