1. What is python?
- popular programming language
- used on server to create web applications
- created by Guido van Rossum, 1991

2. Uses of python
- server to create web application
- used with software to create workflow
- can connect database systems. read and modify files
- used for rapid prototyping, or for production-ready software development


3. Why python?
- works on different platforms (window, mac, linux etc)
- simple syntax
- procedural run, object-oriented or functional way

4. Comments
- # single line
- '''''' multi line

5. variables?
- not need to give any type to the variables & can be changed once declared
- case-sensitive

** Variable name **
a. must start with letter or underscore character
b. names cannot start with number
c. names only contain alpha-numeric characters and underscore(A-z, 0-9 & _)
d. no python keywords should be used


6. Casting 
- add str(), int(), float() 
- check type : type() function 

('' and "" both are same)


1. Camel case
myVariableName="John"
2. Pascal Case
MyVariableName="John"
3. Snake Case
my_variable_name="John"

7. Ways to Assign values 
- x=2;
- x= str(3);
- x,y,z = 3,4,5;


8. global variables : 
- can be used inside & outside function
- all above are global functions

9. Local variables:
- defined inside function are local
- can only be used inside function


10. Data types
* built-in Data types: --> 
- variables can store data of different types, and different types can do different things.
Text type : str
Numeric type : int , float, complex
sequence type : list,tuple, range
mapping type : dict
set types : set, frozenset
boolean type : bool
binary type : bytes, bytearray, memroyview
none type : NoneType

11. Python numbers 
* int
* float
* complex

12. Random Number : there is no random() function in python
- but there is random module that can be used to make random numbers 

ex. 
import random

print(random.randrange(1,10));

13. Casting 
a. int()

b. float()

c. str() - string are array. stores single character in index  
print(x[1]); --> access using index value

- using loops to access the string array
for x in "banana":
print(x)

- string length : len()

print(len(a));

- Check String : check if word or character is present in string

print("hello" in x)

 use if and if not : -> to check if present or not in sentence

- String Slicing: -> 
return range of charaters using slice syntax

start index and end index(exclude)

print(a[2:4]);
print(a[:4]);
print(a[3:])
print(a[-5:-2])
- it will start from backside where 1st index will be -1 

- modify String : -> 
1. upper case
print(a.upper())

2. lower case
print(a.lower());

3. remove whitespace
print(a.strip())

4. Replace string
print(a.replace("H","j"));

5. split string - split string into substring 

print(a.split(","));

- String Concatenation

1. combine two string using + operator 
c = a+b;
print(c)

- format string
cannot combine string and number
txt = "my name is" + age;
print(txt)


# we can combine string and number using f-strings or fomat() method

1. F-String - introduced in python 3.6
--> to specify string as f-string, simply put f in front of string literal, & add curly brackets {} as placeholders for varianles and other operations

txt = f"my name is prapti and i am {age}";
print(txt);

2. placeholders and mosifiers 
- contains variables , operations, functions, modifiers to formate values 

- placeholders can be used to modify number

price = 20;
txt = f"The price is {price:.2f} dollars"
print(txt);


- Escape Characters 
> insert characters that are illegal in string 
> "\"

txt = "We are the so-called \"Vikings\" from the north"

\'
\\
\n
\r
\t
\b
\f
\ooo
\xhh


- String Methods : All string methods return new values. they do not change original string


https://www.w3schools.com/python/python_strings_methods.asp


# Booleans

True and False

print(10>9)
print(10 ==9)

bool() function allows you to evaluate any value, and give True and False in return 

print(bool("Hello"))

almost all values are True except empty values, (), [], {},"", 0 and value None

bool(False)
bool(None)
bool("")
bool(())
bool({})
bool([])

if you have object that is madde from a class with a __len__ function that returns 0 or False

ex. 

class myclass():
    def __len__ (self):
      return 0;

myobj = myclass()
print(bool(myobj))

- function can return boolean value : 

def myFunction():
   return True

print(myFunction())

def myFunction():
   return True

print(myFunction())


def myFunction():
    return True
if myFunction():
    print("YES");
else:
    print("NO!");

# python has many build-in function that returns boolean values,
# like isinstance() function, 

print(" ")
x = 200
print(isinstance(x,int))



- Python Operators: used to perform operations on variables and values

print(10+5)



'''

arithmatic
assignment 
comparison
logical
   - and
   - or
   - not

identity
   - is 
   - is not

membership operators
   - in
   - not in 

Bitwise 

always check for operator precedence

'''


      
# python list

mylist = ["apple","banana","orange"]
print(mylist);

- used to store multiple items in single variables


# 4 Built in data types 

1. List
2. Tuple
3. Set
4. Dictionary


1. List
- items are ordered, changeable, allow duplicate values
- items are indexed, 
first item [0] second [1] etc

* Ordered
lists are ordered, it means that items have a defined order, that order will not change

new items will be placed at the end of list

* Changeable 

list is changeable, we can change, add , and remove items in list after created

* Allow duplicates
lists are indexed, list can have items with same values


thislist = ["apple","orange","cherry", "apple"]
print(thislist);

* list items can be of any datatype

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

* multiple datatype : under single variable

list1 = ["abc",1,True,"male"]
print(list1);

- type() function 
print(type(list1))

- list() constructor - used when creating new list
assigns the list of the variable 

thislist = list(("apple","banana"))
print(thislist);

# Python Collections (Arrays)

* list - collection which is ordered & changable 
- allows duplicate memeber

* Tuple - Collection which is ordered and unchangable 
- allows duplicate memebers

* Set - collection which is unordered, unchaneable* and unindexed
- no duplicate memebers

* dictionary - Collection which is ordered** and changable
- no duplicate memebers


- Set items are unchangeable, but can remove and/or add items 


# Access list items 
- List items are indexeed and you can access them by referring to index number

thislist = ["apple","banan","cherry"]
print(thislist[1])

#Negative index - start from end

-1 = last item (from end)
0 = first item (from start)

print(thislist[-1])


# check if item exists : use "in" keyword
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

