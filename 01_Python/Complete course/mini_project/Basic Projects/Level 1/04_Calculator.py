

# ask the operation to perform  (add, subtract, multiply, divide).
# take values
# give the solution to the operations

def operation():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


def add():
    numbers = input("Enter numbers separated by space: ")
    num_list = [int(x) for x in numbers.split()]
    result = sum(num_list)
    print("Sum is:", result)

def sub():
    numbers = input("Enter numbers separated by spaces : ")
    num_list = [int(x) for x in numbers.split()]
    result = num_list[0]
    for n in num_list[1:]:
        result -= n
    print("Substraction is:", result)

def mul():
    numbers = input("Enter numbers separated by space: ")
    num_list = [int(x) for x in numbers.split()]
    result = 1
    for n in num_list:
        result *= n
    print("Multiplication is :",result)

def div():
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in numbers.split()]
    result = num_list[0]
    try:
        for n in num_list[1:]:
            result /= n
        print("Division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero not allowed!")
   


print("Welcome to the Calculator")


print("Please select an operation:")


operation()
choice = input("Enter your choice (1-4): ")

if choice == '1':
        
    add()

elif choice == '2':
    sub()


elif choice == '3':
  
    mul()


elif choice == '4':

    div()
else:
    print("Successfully generated result !!!!!!!")
