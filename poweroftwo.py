# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

num = int(input("Enter a number: "))

if num > 0:
    while num % 2 == 0:
        num //= 2

    if num == 1:
        print("True")
    else:
        print("False")
else:
    print("False")