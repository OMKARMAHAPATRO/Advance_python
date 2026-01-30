'''
username = input("Enter your username :")
pasword = input("Enter your password :")
if (username == "omkar" and pasword == "1234"):
    print("Login Successful")

else:
    if(username != "omkar" and pasword != "1234"):
        print("Invalid username and password \nLogin Failed !!!")
    elif(username != "omkar"):
        print("Invalid username \nLogin Failed !!!")
    else:
        print("Invalid password \nLogin Failed !!!")
'''

'''
marks = int(input("Enter your marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
'''

# even_odd
'''num = int(input("Enter a number : "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

'''

# factorial of a number
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number to find factorial : "))
result = factorial(n)
print(f"Factorial of {n} is = {result}")

'''

# prime number 
'''

n = int(input("Enter a number to check prime or not : "))
if n > 1:
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
'''

# calculator 
a = int(input("Enter first number: "))
b = int(input("enter the second number : "))
