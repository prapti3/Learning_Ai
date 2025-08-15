# print("hello ")

# comments
'''multiple line comment'''

# Variables & Datatypes 
# a = 34;
# print(type(a))

# input and output
# name = input("name : ")
# print(f"your name is {name}")

# age = int(input("What is you age : "))
# print(f"your age is {age}")
# print(type(age))


# Operator

# conditional statements
# Q1. Accept two numbers and print the greatest between them.
# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))

# if(a>b) :
#     print(" a is Greatest")
# else :
#     print("b is Greatest ")

# Q2. Accept the gender from the user as char and print the respective greeting message
# Ex - Good Morning Sir (on the basis of gender)

# gender = str(input("Enter your Gender : "))
# if(gender == 'female'):
#     print("Good Morning Madam!!")
# else :
#     print("Good Morning Sir!!")



# Q3. Accept an integer and check whether it is an even number or odd.
# num = int(input("Enter the number : "))
# if(num%2 ==0):
#     print("your number is prime")
# else:
#     print("Your number is not prime")


# Q4. Accept name and age from the user. Check if the user is a valid voter or not.



# name = str(input("Enter your name : "))
# age = int(input("Enter your age : "))

# if(age >=18):
#     print("You are a valid voter")
# else :
#     print("You are not valid voter")


# Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)
# year = int(input("Enter the year : "))
# if(year % 400 ==0) or (year % 4 ==0  and year % 100 != 0):
#     print("This is Leap Year")
# else:
#     print("It is not a leap year")

"""
take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold 
@ 0°C to 10°C → "Very Cold 
@ 10°C to 20°C → "Cold 
@ 20°C to 30°C → "Pleasant 
@ 30°C to 40°C → "Hot 
@ Above 40°C → "Very Hot "

"""


# temp = int(input("Enter temperature in Celcius : "))
# if(temp <0):
#     print("Freezing cold  ")
# elif(temp >= 0 and temp <= 10):
#     print("Very Cold ")
# elif(temp > 10 and temp <= 20):
#     print("Cold")
# elif(temp > 20 and temp <= 30):
#     print("Pleasent")
# elif(temp > 30 and temp <= 40):
#     print("hot")
# else:
#     print("Very Hot")


# range(1,10,2)  --> 1,3,5,7,9

# for loop 
# a = "String"
# for i in range(len(a)):
#     print(a[i])

# for i in range(1,6):
#     print(i)

# for char in a:
#     print(char)


# Q1. Accept an integer and Print hello world n times
# n = int(input("Enter your number : "))
# for i in  range(1,n):
#     print(i)


# Q2. Print natural number up to n
# n = int (input("Enter your num : "))
# for i in range(1,n+1):
#     if(i >0):
#         print(i)



# Q3. Reverse for loop. Print n to 1
# n = int(input("Enter the number : "))
# for i in range(n,0,-1):
#     print(i)


# Q4. Take a number as input and print its table
# num = int(input("enter number : "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# Q5. Sum up to n terms

# num = int(input("Enter your number : "))
# total = 0
# for i in range(1,num+1):
#     total += i
# print(total)


# Q6. Factorial of a number
# num = int(input("Enter the number : "))
# result = 1

# for i in range(1,num+1,1):
#     result *= i
#     print(result)

# Q7. Print the sum of all even & odd numbers in a range separately

# num = int(input("Enter your number : "))
# odd =0
# even = 0

# for i in range(1,num+1):
#     if(i%2 == 0 ):
#         even += i
#     elif(i%2 != 0):
#         odd +=i

# print(f"Even number are : {even}\n Odd numbers are : {odd}")


# Q8. Print all the factors of a number


# num = int(input("Enter your number : "))
# for i in range(1,num+1):
#     if(num%i ==0):
#         print(i)



# Q9. Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself

# num = int(input("Enter the number : "))
# n=0
# for i in range (1,num):
#     if(num%i == 0):
#         n +=i

# if(n == num):
#     print(f"{num} is a perfect number")
# elif(n != num):
#     print(f"{num} it is not a perfect number")


# Q10. Check wether the number is prime or not

# num = int(input("Enter the number : "))

# if num <= 1:
#     print(f"{num} is not a prime number")
# else:
#     is_prime = True
#     for i in range(2, num):  # check divisors from 2 to num-1
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")


