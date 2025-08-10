# simple print statement 
print("Hello world");

# if-else statements 
if(5>2):
    print("five is bigger than 2");

else:
    print("error");


#comment
'''multi
line '''



#Variables: -> containers for storing data values
x =5;
y = "HaveFun";

print(x);
print(y);

#variables dont need any type& can change type after they have been set


# casting : if we have to specify the datatype of a variable
a= str(3);
b =int(2);
z= float(3);


# get the Types of variables : type() function
print(type(a));
print(type(b));
print(type(z));

# "" and '' both are same

# Case sensitive : variables names are case-sensitive

g=4;
G="Sally";
# both are different 


# assign multiple variables
x,y,z = "Orange","Banana","Mango";
print(x);
print(y);


# x,y,z = "ORange"; == error 
# equal values and values should be there


#list:
fruits = ["apple","banana","Cherry"];
x,y,z = fruits;
print(x);
print(y);

#output ways
print(x);
print(x,y,z);
print(x+y+z);
print(x+ " " + y + " "+z);


'''
Global Variables: variables that are created outside of a function
-> all above variables are global variables 
-> can be used by everyone, both inside of function & outside



'''

x = "awesome";

def func():
    x = "fun code";
    print("Python is " + x);

func();

print("Python is " + x);

#example


#global keyword :  to create variables inside function which are usually local to function 
# but to create global variables inside function use "global" keyword
y = "Learning";

def myFun():
    global y;
    y = "learn";
    print(y +" "+ "python");

myFun();

print(y + " " + "python2")


# to change values of variables inside function use global keyword 
# so that variables can be accessed outside the functions

#y = "Learning";

x = "Hello world"  # string
x = 20 # number
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana"] # list
x = ("apple", "banana") # tuple
x = range(6);  #range
x = {"name" : "John", "age" : 30} # dict
x = {"apple", " banana","cherry"} # set
x = frozenset ({"apple","banana", "cherry"});  # frozenset
x = True  # bool
x = b"Hello";   # bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5));  # memoryview
x = None;   # NoneType


# random number

import random

print(random.randrange(1,10));


# casting
#1. int()
x = int(2);
y = int(2.3);
z = int("3");

print(type(x)); # 2
print(type(y));  # 2
print(type(z));  # 3

# 2. float()

x = float(2); # 2.0
y = float(2.3); # 2.3
z = str("2.3") # 2.3

print(" ")
print(type(x))
print(x)
print(type(y))
print(y)
print(type(z))
print(z)


# 3. string : 'hello' and "hello"

print("It's prapti here");
print("he is called 'Johny'")
# prints the sentence as it is in ""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''


print(a);
# works for '''''' and """"""

'''
# String are Array
#        python does not have character datatype
 = single character is simply string with length of 1
 
#  
'''

a = "Hello world";
print(a[1]);


# looping through string
# for x in "banana":
    # print(x);

# string length

print(len(a));


# check string : if word or character is present

txt = "the best things in like are free!"
print("free" in txt);

# use if
if "free" in txt:
    print("Yes, 'free' is present.");


# if not
print("expensive" not in txt);

if "expensive" not in txt:
    print("Yes! it is not present.")


print(" ")
# String slicing 
print(a[2:4]);
print(a[:4]);
print(a[3:])
print(a[-5:-2])

#split string

print(a.split(","));

# formate string
# this will give error 
age = 30;
# txt = "my name is" + age;
# print(txt)


#use f-string
txt = f"my name is prapti and i am {age}";
print(txt);


#placeholder and modifiers 
price = 20;
txt = f"The price is {price:.2f} dollars"
print(txt);


# {} can contains python code , like maths operation
'''
{20*30}
{20+30}
{20-30}
'''


txt = "We are the so-called \"Vikings\" from the north"
print(txt)


# boolean
print(10>6)
print(10==9)


# function return boolean 

class myclass():
    def __len__ (self):
      return 0;

myobj = myclass()
print(bool(myobj))



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


# operator 
print(2+3)

#1. Aritmatic -> 
print(1+2)
print(3-2)

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


# list: multiple items stored in single variables
# changable, allows duplicate, ordered 
thislist = ["apple","orange","cherry", "apple"]
print(thislist);

# length od list: len() function

print(len(thislist))

# list items can be of any datatype

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# multiple datatype in single variable 
list1 = ["abc",1,True,"male"]
print(list1);
print(type(list1))

thislist = list(("apple","banana"))
print(thislist);

# access list items
print(thislist[0]);

# from backword
print(thislist[-1])

print(thislist[1:3])
print(thislist[:3])
print(thislist[2:])
print(thislist[:])

# check if item exists : use "in" keyword
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")



