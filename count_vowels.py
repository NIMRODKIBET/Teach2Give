# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.


sentence = input("Enter your sentence: ")
string = sentence.lower()
print(string)
count = 0
vowels = ["a", "e", "o", "u"]
for char in string :
    if char in vowels:
        count = count+1
print("The number of vowels in the given sentence is: ", count)