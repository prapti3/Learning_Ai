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
