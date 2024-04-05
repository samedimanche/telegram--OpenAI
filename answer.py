n = int(input('Enter int n: '))
print("#1 Result:", n+n*n+n*n*n)

a = [1, 1, 2, 3, 5, 8, 13, 21, 22, 34, 55, 237, 89]
print("#2 a:", a)
list=[]
for i in a:
    if i != 237:
        if i % 2 ==0:
            list.append(i)
    else:
        print("list % 2==0 :", list)
        print("STOP Error: 237")
        break
print("--------------------------------")
from fractions import Fraction
real_number = 14.375
fraction = Fraction(real_number).limit_denominator()
print("#3 ",f'{real_number} = {fraction.numerator}/{fraction.denominator}')
def get_time_from_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{days}:{hours}:{minutes}:{seconds}'
total_seconds = 123456789
time_str = get_time_from_seconds(total_seconds)
print("#4 ",time_str)
if n %2 ==0:
    print("#5 ",n,"is even")
else:
    print("#5 ",n,"is odd")
print("--------------------------------")
z = int(input("Enter second number: "))
v = input("Enter sign + or - or / or * : ")
if v == "+":
    print("#6 ",n,"+",z,"=",n+z)
elif v == "-":
    print("#6 ",n,"-",z,"=",n-z)
elif v == "/":
    print("#6 ",n,"/",z,"=",n/z)
elif v == "*":
    print("#6 ",n,"*",z,"=",n*z)
else:
    print("#6 Error: Wrong sign")
print("--------------------------------")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
choice = input("Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius: ")
if choice == '1':
    celsius = float(input("Enter the temperature in degrees Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("#7 ",f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("#7 ",f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
import random
print("#8 ",random.randint(0,100))