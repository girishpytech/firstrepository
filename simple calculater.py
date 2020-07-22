print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.exit")

while True:
    choice_process=int(input("put the process number down here:"))
    if choice_process >=1 and choice_process < 5:
        print("enter two numbers>>>>")
        num1=float(input("input the first number:"))
        num2=float(input("input the second number:"))
        if choice_process==1:
            print("the addition is ", num1+num2)

        elif choice_process==2:
            print("the substarction is" , num1-num2)
        elif choice_process==3:
            print("the multiplication is ", num1*num2)
        elif choice_process==4:
            print("the division is ", num1/num2)
    elif choice_process == 5:
        break
    else:
        print("you have entered a wrong choice check it again !!!!")
