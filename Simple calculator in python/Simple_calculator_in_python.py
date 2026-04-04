a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose your operation:")
print("+ : Add")
print("- : Sub")
print("* : Mult")
print("/ : Div")
c = input("Enter your choice: ")

if c == "+":
    print("Sum is:", a + b)
elif c == "-":
    print("Sub is:", a - b)
elif c == "*":
    print("Multi is:", a * b)
elif c == "/":
    print("Div is:", a / b)
else:
    print("Invalid choice")
