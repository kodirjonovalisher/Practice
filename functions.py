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
