
left = 3.14

print("Hello I am going to tell you about my pies.") 
def pies(available,eaten):
    left = available - eaten
    return left
print(str(left) + " is an example of the variable assigned outside the function.")
print(str(pies(60,20)) + " is an example a function calling the value of it's variables.")
print(str(pies(70,25)) + " as is this.")
print(str(pies(100,10)) + " and this.")

print("Please look at the code and see this is a demonstration of how scoping works inside and outside of a function.")