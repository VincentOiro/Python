person = {
    'name': 'vin',
    'age': 30,
    'home': 'kisumu'
}

print(person.items()) 

for key,value in person.items():
    print(f'{key}: {value}') 
    
    
languages=['python','javascript','python','c++']
for index,language in enumerate(languages):
    print(index+1,language)
    
    
# Accessing values by keys