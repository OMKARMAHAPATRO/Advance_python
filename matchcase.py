# example 1
'''
Docstring for matchcase
choice = input("Enter your choice (apple/banana/cherry): ")
match choice : 
    case "apple":
        print("apple")
    case "banana":
        print("bannana")
    case "cherry":
        print("cherry")
    case _:
        print("invalid choice")

'''

# example 2 
'''
day = int(input("Enter day number (1-7): "))
match day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

'''

# example 3
'''
color = input("Enter the color :")
match color : 
    case "red":
        print("stop")
    case "yellow":
        print("get ready to go ")
    case "green":
        print("go")
    case _:
        print("you are a bockachoda")
'''

# example 4 : calculator using match case
'''
a = int(input("Enter first number: "))
b = int(input("enter the second number : "))
operation = input("Enter operation (+, -, *, /): ")
match operation :
    case "+" :
        print(f"sum : {a+b}")
    case "-" :
        print(f"subtraction : {a-b}")
    case "*" :
        print(f"product : {a*b}")
    case "/" :
        print(f"division : {a/b}")
    case _ :
        print("invalid operation")
'''

# example 5 : cheack the number is  positive or not.
'''
n = int(input("Enter a number: "))
match n :
    case _ if n > 0 :
        print(f"{n} is positive")
    case _ if n == 0 :
        print(f"{n} is zero")
    case _ :
        print(f"{n} is negative")
'''

# example 6 : cheack odd or even 
'''
n = int(input("Enter a number: "))
match n % 2 :
    case 0 :
        print(f"{n} is even")
    case 1 :
        print(f"{n} is odd") 
'''

# example 7 : print vowels and consonent by using match case (only character)
'''
word = input("Enter a letter: ").lower()
match word :
    case "a" | "e" | "i" | "o" | "u" :
        print(f"{word} is a vowel")
    case _ :
        print(f"{word} is a consonent")
'''

# example 7.1 : print vowels and consonent by using match case ( for both char and word )
'''
word = input("Enter a word: ").lower()

vowels = ""
consonants = ""

for ch in word:
    match ch:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            vowels += ch
        case _:
            consonants += ch

print("Vowels:", vowels)
print("Consonants:", consonants)

'''

# example 8 : Login system by using match case
username = input("Enter username: ")
password = input("Enter password: ")
match (username , password ) :
    case ("admin" , "admin123") :
        print("Login Successful")
    case ("admin" , _) :
        print("Invalid password \n Login Failed !!!")
    case _ :
        print(" Please enter valid username \n Login Failed !!!")
