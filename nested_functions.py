def parent(name='Vin'):
    print(f'My name is {name}')
    def child(name='joe'):
        print(f'{name} is a child')
    child() 
    
    
parent() 

def dog():
    def speak():
        return 'Woof!'
    return speak


woof = dog()
print(woof())
        
