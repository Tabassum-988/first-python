#check if string start with a substring
text="Hello World"
print(text.startswith("Hello"))#return True/False
##check if string start with a substring
print(text.endswith("World"))
#find the position of a substring
print(text.find("World"))#find starting index of the substring 
#find occurrences of a substring
print(text.count('l')) 
#is alphanumeric
print(text.isalnum())
#is alphabetic
print(text.isalpha())
#is numeric
print(text.isdigit())
#whitespace
print(text.isspace())
#titlecase
print(text.istitle())