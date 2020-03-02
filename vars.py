#Below are the following data types present in Python

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

x = str("Data") #Here the data type has been manually set by us

def num_types():
    num1 = 1 #int
    num2 = 2.8 #float
    num3 = 1j #complex - complex uses j instead of i

    y  = type(num1) #Gives the data type for that variable

    print(y)

num_types()