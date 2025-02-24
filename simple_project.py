#Greeting project
name=input("Enter your name :")
print("Hello "+ name + " !")



#simple calculator
First_number=input("Enter first number :")
Second_number=input("Enter second number :")
#Explicit conversion because input function carry string
First_number=int(First_number)
Second_number=int(Second_number)
Sum=First_number+Second_number
print("Sum : " ,Sum)
Sub=First_number-Second_number
print("Sub :" ,Sub)


#Temperature Converter
Celsious=float(input("Enter temperature in celsious :"))
Fahrenheit=((Celsious*9)/5)+32
print("Fahrenheit=",Fahrenheit)


#Simple interest calculator
Principle=float(input("Enter the principle :"))
Rate=float(input("Enter the rate of interest :"))
Time=float(input("Enter the time (in years) :"))
Interest=(Principle*Rate*Time)/100
print("Interest :",Interest)

