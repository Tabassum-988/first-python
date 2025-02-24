"""
Immutable data type :  Assign different location if same variable hold different value.
                       and the value isn't modified create another 
                       -Integer,Float,String,Tuple,Frozenset
"""

a=5
first_location=id(a)
print(first_location)
print(a)
a=6
second_location=id(a)
print(second_location)
print(a)


#Mutable data type : location won't be different
#                   -list,set,dictionaries

l=[1,2,3,4]
first_location=id(l)
print(first_location)
l[0]=4
second_location=id(l)
print(second_location)
