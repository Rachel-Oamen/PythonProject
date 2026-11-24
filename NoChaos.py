# Average
total = 0
count = 0

number = float(input("Enter any digit: "))

print("Enter 0 to exit the program")

while number != 0:

    total = total + number

    count = count + 1

    average = total / count

    print("Average is =", average)

    number = float(input("Enter a Number Again: "))
