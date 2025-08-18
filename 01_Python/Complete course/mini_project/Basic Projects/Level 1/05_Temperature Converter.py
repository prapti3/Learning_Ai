
# 5. Temperature Converter
#    - Convert Celsius ↔ Fahrenheit ↔ Kelvin.


# take temp in celsius or Fahrenheit or kelvin
# convert it into 2 alternatives 
# give all 3 temp result


# take temp in celsius or fahrenheit or kelvin

print("***** Hello to Temp converter ******** ")
print(" ")

print("Press 1 for Celsius ")
print("Press 2 for Fahrenheit ")
print("Press 3 for Kelvin ")


select_num = int(input("Select the Temp you are going to give between 1-3:- "))



def cel():
    Fahrenheit = (temp * (9/5)) +32
    print(f"{temp}\u00B0C in Fahrenheit is {round(Fahrenheit)}\u00B0F")
    
    
    kelvin = (temp + 273.15)
    print(f"{temp}\u00B0C in Kelvin is {kelvin}K ")

    
    
def fah():
    Celsius = (temp-32)* (5/9)
    print(f"{temp}\u00B0F in Celsius is {round(Celsius)}\u00B0C ")
    
    kelvin = (temp - 32) * (5/9) + 273.15
    print(f"{temp}\u00B0F in Kelvin is {kelvin}K")
    
def kelvin():
    Celsius = (temp -273.15)
    print(f"{temp} in Celsius is {round(Celsius)}\u00B0C")
    
    Fahrenheit = (Celsius *(9/5)) +32
    print(f"{temp}K in Fahrenheit is {Fahrenheit:.2f}\u00B0F ")
    


if select_num ==1:
    temp = int(input("Give the temp in Celsius:- "))
    cel()
    


elif select_num == 2:
    temp = float(input("Give the temp Fahrenheit:- "))
    fah()
    
elif select_num == 3:
    temp = float(input("Give the temp Kelvin:- "))
    kelvin()
    
else:
    print("Invalid choice ! Please select 1, 2, or 3.")
    
    
    

