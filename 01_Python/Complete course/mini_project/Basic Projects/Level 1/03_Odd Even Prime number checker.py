

# 4. Odd/Even & Prime Checker
#    - Input a number and check if it’s odd/even or prime.


number = int(input("Enter the number :- "))
if number >0:
    if number % 2 ==0:
        print(f"{number} is Even")
    elif number %2 != 0:
        print(f"{number} is Odd")
 
 
 # Prime check
    if number == 1:
        print("1 is neither Prime nor Composite")
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):  # check divisors up to sqrt(number)
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is Prime")
        else:
            print(f"{number} is Not Prime")

elif number < 0:
    print(f"{number} is Too Low. Please enter number greater than 0")
        
