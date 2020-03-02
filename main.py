#Python is a programming language

#It is different from some other programming languages because it does not use semi-colons to end a line.
#There are also no curly brackets for scopes. Instead a : is used

print("Hello, world!") #This single lline can run. It does not need to be placed in a main method


#Indentation in Python is important as it defines scopes/blocks of code

if 1 > 0:
    print("1 is more than none")

#Variable types are not declared

var1 = "A random string"
var2 = "which is just boring"

print(var1)
print(var2)

x, y, z = 1, 2, 3

#print("This is print statement number " + x) - Statement does not work because string can only concatenate to another string

#Strings can be concatenated simply using a +

var3 = var1 + var2

print(var3)