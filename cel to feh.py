celsius = float(input('enter the temperature in celsius:'))
print("choose your option:")
print("1.covert celsius to fahrenheit")
print("2.covert celsius to kelvin")
choose = input("choose 1 or 2")
if choose == 1:
    fahrenheit = (celsius * 9/5) +32
    print("The fahrenheit is:" ,fahrenheit )
elif choose == 2:
    kelvin = celsius + 273.15
    print("The kelvin is:",kelvin)
else:
    ("Invaild input")