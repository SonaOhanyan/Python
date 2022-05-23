''' Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
Sample Output:
Input the temperature you like to convert? (e.g., 45F, 102C etc.) : 104f
The temperature in Celsius is 40 degrees'''

temp = float(input("Input the temperature(only numbers) you like to convert?: "))
unit = input("Enter the unit ('c' for Celsius, 'f' for Fahrenheit): ")
if unit == 'c':
    f = 9/5 * temp + 32
    print("The temperature in Fahrenge is: ", f)
elif unit == 'f':
    c = 5/9 * (temp-32)
    print("The temperature in Celsius is: ", c)
else:
    print("Enter the right symbols in each filed")
    
