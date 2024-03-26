sentence=input('Enter a sentence: ')

print(len(sentence) )

file_name=input("Enter file name: ")
file_name=file_name+".txt"

with open (file_name, 'w') as f:  # with is used for automatic resource management.
    f.write("%s\n" % sentence)   # write() writes the string to
    f.close()
contents=open(file_name).read()
print(contents)
print(f"you've written {len(sentence)} characters in {file_name}") 