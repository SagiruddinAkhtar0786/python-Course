#num = int(input("Enter a number: "))


""" try:
    num = int(num)  # Attempt to convert the input to an integer
    print("You entered:", num) 
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
except ValueError as e:
    print("Invalid input! Please enter a valid integer.")
    print("Error:", e)
 """

""" 
try:
    result = 10 / num  # Attempt to divide by the input number
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
 """
l = [3,4,5,73,3]
""" try:
    for i, value in enumerate(l):
        print(i, value)
except Exception as e:
    print("invalid number",e)
finally :
    print("i will be printed always")
 """

""" try :
    for i in range(7):
        print(l[i+1])
except Exception as e:
        print("error : ",e)
finally:
    print("always executable") """


a = int(input("enter any value between 5 an d 9"))
if(a < 7 or a > 9):
    raise ValueError("there is error with invalid number")