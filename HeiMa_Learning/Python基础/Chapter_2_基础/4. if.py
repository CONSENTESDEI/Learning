# 基础
score = 700
if score > 700:
    print(f"Your score is {score}")

# 进阶 else elif
# 闰年判断
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")