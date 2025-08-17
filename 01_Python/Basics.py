import random
# import emoji


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


# Q11. Reverse a string without using in build functions.

# name = str(input("Enter your name : "))
# rev_string = ""
# for char in name:
#     rev_string = char+rev_string

# print(rev_string)


# Q12. Check string is Pallindrome or not

# name = str(input("Enter the string : "))
# reverse_str=""

# for char in name:
#     reverse_str = char+reverse_str

# if(reverse_str == name):
#     print(f"{name} is a palindrom ")
# else:
#     print(f"{name} is not a palindrom")



# Q13. Count all letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve"

# str1 = "P@#yn26at^&i5ve"

# letters = 0
# digits = 0
# symbols = 0

# for char in str1:
#     if char.isalpha():       # check if letter
#         letters += 1
#     elif char.isdigit():     # check if digit
#         digits += 1
#     else:                    # everything else = special symbol
#         symbols += 1


# print(f"Letter : {letters}")
# print(f"Digits : {digits}")
# print(f"Symbols : {symbols}")

# While loop : -->

# a = 1
# while a<=30:
#     print(a)
#     a+=1






# Q1. Separate each digit of a number and print it on the new line

# num = int(input("Enter the number : "))
# while num > 0:
#     print(num%10)
#     num //= 10


# Q2. Accept a number and print its reverse


# num = int(input("Enter the number : "))
# rev =0

# while num > 0:
#     rev = rev *10 + num%10
#     num //= 10

# print(rev)


# Q3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)

# num = int(input("Enter the number : "))

# rev =0
# copy =num

# while num > 0:
#     rev= rev *10 + num%10
#     num //= 10

# if(rev == copy):
#     print(f"{copy} is a palindrome")
# elif(rev != copy):
#     print(f"{copy} is not a palindrome")


# Q4. Create a random number guessing game with python.

# random_number = random.randint(1,100)
# guess_number =int(input("Guess the random number : "))

# if(random_number == guess_number):
#     print("YESSSSS! You win 🎉")
# elif(random_number != guess_number):
#     print("ohhhh!! Better luck next time 😢")

'''Functions'''

# def greet(name):
#     print(f"Hello {name}, welcome to the world of Python!")

# greet("Prapti")


# def add(a,b):
#     return a+b

# print(add(1,2))

# def intro(name = "akaksh"):
#     print(f"Hello, {name}")

# intro()



'''  Data Structures '''

# build in Data structures

# 1. List
'''
my_list = [1, 2, 3, 4, 5]
my_list.append(6) # Add an element to the end
my_list.insert(2,15) # Insert an element at index 2
my_list.remove(2) # Remove the first occurrence of 2
my_list.extend([7,8,9]) # Extend the list with another list
popped_item = my_list.pop() # Remove and return the last item
index = my_list.index(4) # Get the index of the first occurrence of 4
my_list.append(5) # Add 5 to the end
count_5 = my_list.count(5) # Count occurrences of 5
my_list.sort() # Sort the list in ascending order
my_list.reverse() # Reverse the list
new_list = my_list.copy() # Create a shallow copy of the list
# my_list.clear() # Remove all elements from the list



print(f"my List is : {my_list}")
print(f"Popped items is : {popped_item}")
print(f"index value of 4 is : {index}")
print(f"count how many 5 are there : {count_5}")
print(f"New list : {new_list}")



'''



# Q1. Print positive and negative elements of an List?

# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
# positive_numbers = []
# negative_numbers = []

# for num in numbers:
#     if num >= 0:
#         positive_numbers.append(num )
#     else:
#         negative_numbers.append(num)

# print(f"Positive numbers: {positive_numbers}")
# print(f"Negative numbers: {negative_numbers}")

#Q3. Mean of the list

# my_list = [1,2,3,4,-5,6,7]
# total_count = 0
# add_items = 0
# mean_num =0

# for i in my_list:
#     # if i > 0:
#         total_count+=1
#         add_items = add_items+i
    

# mean_num = add_items // total_count

# print(f"Mean of the list is : {mean_num}")



# Q4. Find the greatest element and print its index too?

# my_list = [1,2,3,4,5,6]

# largest_num = my_list[0]
# index_largestNum =0

# for i in my_list:
#     for j in my_list:
#         if i>j:
#             largest_num = i
    

# print(largest_num)
# index_largestNum = my_list.index(largest_num)
# print(index_largestNum)


# *********** different solution ************************


# l = [1,2,3,4,5,6]

# largest = l[0]
# index= 0
# for i in range(len(l)):
#     if l[i] >largest:
#         largest = l[i]
#         index= i
        
# print(index)
# print(largest)




# Q5. Find the second greatest element?

# print(dir(list))
# help(list)

# l = [11,32,43,14,25,36]

# largest = l[0]
# sec_largest = l[0]

# # l.sort()   sort the list first

# for i in range(len(l)):
#     if l[i] >= largest:
#         sec_largest = largest
#         largest = l[i]
        

# print(f"Largest number is : {largest} and Second largest is : {sec_largest}")




# Q5.Check if List is sorted or not.

# l = [11, 32, 43, 14, 25, 36]

# is_sorted = True
# for i in range(len(l) - 1):
#     if l[i] > l[i + 1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("Your list is sorted")
# else:
#     print("Your list is not sorted")



''' Tuple 

t = (1,2,2,3,4)
print(type(t))

index = t.index(3)
print(index)

count_2 = t.count(2)
print(count_2)


'''




'''   Set  


s = {1,2,3,4,"Hello",5}
print(type(s))
print(s)

print(hash("Hello"))

# set mmethods 
s.add(9)
s.remove(3)
s.discard(5)
s.pop() # removes random values
 

A = {1,2,3}
B = {3,4,5}

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_diff = A.symmetric_difference(B)

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)


for i in s:
    print(i)


'''


''' Dictionary '''

# dict = {1:10,2:20,3:30,4:40}
# for i in dict:
#     print(i,":", dict[i])


# help(dict)
# Q1. Write a Python script to merge two Python dictionaries?

dict1 = {1:10,2:20}
dict2 = {3:30,4:40,5:50,6:60}

# merged_dict = {**dict1, **dict2}
# print(merged_dict)


# for i in dict1:
#      print(dict1[i]) #values
#      print(i) #keys


#Q2. Write a Python program to sum all the values in a dictionary?

# sum =0


# for i in dict1:
#      sum = sum + dict1[i]
    
# print(sum)



# Q3. Count the frequency of each element.

# a = [ 1,1,1,2,2,2,2,3,3,3,4,4,4,5]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

# -----

# num = {1:20, 2:40, 3: 50, 4:30}

# num[2] = 1000  
# print(num)

# print(num.items())



# Q4. Write a Python program to combine two dictionary by adding values for common keys.

# d1 = {1:10,2:20,3:30}
# d2 = {3:30,4:40}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]


# print()


'''

  Exception Handling  


# 1. Errors -->

> two types of errors 

a. Syntax error
b. logical error


> Syntax error --> wrong syntax 
> indentation error --> spacing errors

Errors cannot be handled but 
Exception can be handled


Exception -->
- occures during execution of program


print("Start")
print(10/0)
print("End")


'''


# a = int(input("tell your number :- "))
# try:
#     print(10/a)
# # except ZeroDivisionError:
# except Exception as e:
#     # print("Sorry you cannot divide with 0")
#     print(e)

# else:
#     print("Good there is no error")

# finally:
#     print("Wowww , looking good !!!!!!!!!")


# print(f"OK i have divided the number : {a}")

#  ----------------

# age = int(input("tell me your number : "))

# try: 
#     if age < 10 or age > 18:
#         raise ValueError("age must be between 10 and 18")
#     else:
#         print("!!!! Welcome to club !!!!")

# except Exception as err:
#     print(f"an error occured : {err}")


# --------------------


'''

***** File handling ********
CRUD

open() function - to open the file
r - read(default) 
w - write
a - Append
x - Create new file, fails if it exists



 '''


file= open("myfile.txt",'r')
print(file.read())    # read entire file









