#!/usr/bin/python3
#My simple calculator

num1 = int(input("Enter first number: "))
op = input("Enter operation: ")
num2 = int(input("Enter second number: "))

if op == '+':
    add = num1 + num2
    print(add)

elif op == '-':
    sub = num1 - num2
    print(sub)

elif op == '/':
    div = num1 / num2
    print(div)

elif op == '*':
    mul = num1 * num2
    print(mul)

else:
    print("Incorrect operation.")
