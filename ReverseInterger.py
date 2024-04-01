# Question 5: Reverse Integer

# Write a program that takes an integer as input and returns an integer with reversed digit ordering.


n = int(input("Enter an integer: "))

rev = 0
while (n>0):
    r= n % 10
    rev = rev*10+r
    n = n//10
print("reversed integer is: ", rev  )