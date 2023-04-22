# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# Sample value of n is 5
# Expected Result: 615

my_integer_input = float(input("Please provide a whole number: "))
my_integer = int(my_integer_input)
by_11 = my_integer*11
by_111 = my_integer*111

answer = my_integer + by_11 + by_111

print("Using the number "+str(my_integer)+" to find the result of "+str(my_integer)+" + "+str(by_11)+" + "+str(by_111))
print("The answer is: "+str(answer))

# end assignment