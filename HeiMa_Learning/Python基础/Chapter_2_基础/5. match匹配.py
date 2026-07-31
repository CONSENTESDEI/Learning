# match和switch作用相同

# 日期计算
day = input("Enter a day: ")
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
        print("Wed")
    case 4:
        print("Thur")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _: # 其他情况
        print("Invalid input")

# 算数
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
oper = input("Enter a operator: ")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("Invalid input")
