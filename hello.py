# print('Hello buana')
def mazematik():
    name=input('what is your name?')
    print(f"Your name is {name} ")

# mazematik()

with open ("file.txt", 'w') as doc:
    doc.write('This is a file created using python computer programming language')

# Close the file and reopen it in read mode
doc.close()

with open ("file.txt", 'a') as doc:
    doc.write(f'\n I love to code in Python')
   
    
doc.close()   
with open ("file.txt", 'r') as doc:
    contents=doc.read()

print(contents)