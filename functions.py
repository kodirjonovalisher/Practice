''' Functions
 Define vs Call
 Parametr vs Argument
 Keyword and default arguments
 Scope
'''

print("==== Define and Call====")
# build in functio > print() type()
# function - reusable block of code!
# instead of block {} in JAVA, Python uses identation!

# Define - build, parametr bu (a)


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is exucuted")
    return f"Hi {b}"


# Call - execute,  argument (Alisher,ALex)
result1 = greet("Alisher")
print("result1:", result1)

result2 = greeting("Alex")
print("result2:", result2)


print("====Keyword and default arguments")

# Define


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"


# Call
result3 = give_greet(name="Alisher", age=28)
print("result3:", result3)

result4 = give_greet('Alisher')
print("result4:", result4)


print("==== scope =====")
b = 100  # 3

# Define


def calculate(a):  # 2
    c = a*b  # 1
    print(f"the c value: {c}")


# Call
calculate(5)
