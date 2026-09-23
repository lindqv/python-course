
# 1. 
print("Python documentation"[:6]) # Python
print("Python documentation"[7:]) # documentation
print("Python documentation"[7:15]) # document
print("Python documentation"[:6:2]) # Pto
print("Python documentation"[-3]) # i
print("Python documentation"[6]) # " "
print("Python documentation"[:6:-1]) # noitatnemucod
print("Python documentation"[::4]) # Pooet

# 2. 
string = "Artificial Intelligence"
print(string[:10]) # First 10 characters. Output: Artificial
print(string[11:]) # From index 11 to the end of the string. Output: Intelligence
print(string[::3]) # Every third letter. Output: Aiclnlgc
print(string[::-1]) # The string reversed. Output: ecnegilletnI laicifitrA
print(string[:10:-1]) # Reversed, from index 10 to the end. Output: ecnegilletnI
print(string[10::-1]) # Reversed, from the start to index 10. Output:  laicifitrA
print(string[0] + string[11]) # The characters at index 0 and 11. Output: AI

# 3.
# Splitting a string given a separating character
shopping = "bread, tea, almonds"
items = shopping.split(",")
print("Items to buy:", items)

# Removing whitespace
user_input = "   hello       "
no_whitespace = user_input.strip()
print("Without whitespace", no_whitespace)

# Replacing parts of a string
new_shopping = shopping.replace("almonds", "peanuts")
print("Replaced string", new_shopping)

# 4.
greeting = "hello"
# The line below causes a type error, since strings are immutable.
#greeting[0] = "H" 
modified_greeting = "H" + greeting[1:]
print("Modified string", modified_greeting)