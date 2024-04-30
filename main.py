"""
Multiplication Table # I am really sorry for this mess.
"""
# Provide your solution here
def print_multiplication_table(a: int, b: int):     # not used yet
    return (a * b)


a = int(input("For which number would you like to know its multiplication table? "))
b = int(input("How many multiplications would you like to know? "))

while b > 0:# wrong order
    print(b, "*", a, "=", a*b)
    b -= 1

else: # I tried it with conditionals first
    print("Number and rows cannot be less than 1.")
"""
Palindromes
"""
# Provide your solution here

# Press the green button in the gutter to run the script. (test here)
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

#def is_palindrome(a: str)
    #if word
    #return(b)

#while True:
#    word = input("Type a word: ")

###############################################################

#def print_multiplication_table(a: int, b: int):
#    return(a*b)

#def row_counter():
#    while True:
#        i = 1
#        print(i)
#        i += 1

#a = row_counter
#result = print_multiplication_table(int,6)
#print(a, "*", b, "=", result)


def print_multiplication_table(a: int, b: int):     # not used yet
    return (a * b)


a = int(input("For which number would you like to know its multiplication table? "))
b = int(input("How many multiplications would you like to know? "))

while b > 0:# wrong order
    print(b, "*", a, "=", a*b)
    b -= 1

else: # I tried it with conditionals first
    print("Number and rows cannot be less than 1.")


# if b > 0:
#    while True: # or while b>0??
#        print(b, "*", a, "=", a * b)
#        b -= 1
#else:
#    print("Number and rows cannot be less than 1.")




def print_multiplication_table(a: int, b: int):
    while b > 0:  # wrong order
        print(b, "*", a, "=", a * b)
        b -= 1

if a >= 0 and b >= 0:
    print_multiplcattion_table(a,b)
