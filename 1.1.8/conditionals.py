num1 = 6
num2 = 6

signal = "107.4 GreenFN Radio"

true = signal

# Header> if booleanStatement:
if num1 > num2:
    # Body: Holds the statements to execute
    # everything in the same tab level is in the body
    print("Num1 is bigger")
# Elif: Stands for else if. Check the first condition, then check them in the order shown
elif num2 > num1:
    print("Num2 is bigger")
else:
    print(true)