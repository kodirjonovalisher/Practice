# Dunder __builtins__, __init__
message = "Python: Everything is object"
print(message)

result = type(message)
print("result:", result)

''' In Python , there are builtin tools:
(1) Types > int float str list dict
(2) Functions > print() len() input() type() str() int()
(3) Constants > True False None
'''
print(dir(__builtins__))
