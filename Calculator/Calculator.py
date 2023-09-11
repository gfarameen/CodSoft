#  CACULATOR
# Function to perform operations:
def calculator(num1, operator, num2):
    if operator== "+":
        result= num1+num2
    elif operator == "-":
        result=num1-num2
    elif operator == "/":
        if num2!=0:
          result=num1/num2
        else:
            print("Denominator can't be zero")   
    elif operator == "*":
        result=num1*num2
    else:
        print("Invalid move") 
    return result 

# Taking input from user
num1= float(input("Enter First Number:"))
num2= float(input("Enter second Number:"))
operator= (input("Enter operation you want to perform(+, -, /, *):"))

# Calling function
Result= calculator(num1, operator, num2)
print(f"{num1} {operator} {num2} = {Result}")