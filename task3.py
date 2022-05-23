'''Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73 '''

h = int(input("Enter a dog's age in human years: " ))
if 0 < h <= 2:
    d = (h*10.5)
    print("The dog's age in human years is: ", d)
elif h > 2:
    d = (h-2)*4 + 21 #21 is from two 10.5 years
    print("The dog's age in human years is: ", d)
else:
    print ("It's impossible to calculate :|")
