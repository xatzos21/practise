# x = 3
# y = 4

# z = x + y
# print(z)

# def sum(n, n1):
#     return n + n1

# x = 3
# y = 4
# print(sum3(x, y))

def sum(n, n1):
    return n + n1

def sum1(n2,n3):
    return n2 - n3

def sum2(n4,n5):
    return n4 * n5

def sum3(n6,n7):
    return n6 / n7

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = str(input("Choose action +,-,*,/ "))
if z == "+":
    print("Result is: ", sum(x,y))
elif z == "-":
    print("Result is: ", sum1(x,y))
elif z == "*":
    print("Result is: ", sum2(x,y))
elif z == "/":
    print("Result is: ", sum3(x,y))
else:
    print("Wrong input!")