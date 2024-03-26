# Generators are a special kind of function that return a generator object
# A generator object can be iterated over, yielding a value each time

def count_up_to(n):
    # The generator function is defined with the 'yield' keyword
    # Instead of returning a list, the function yields one value at a time
    # Each time the generator is called, it continues from where it left off
    # and yields the next value
    while n > 0:
        yield n
        n -= 1

# Create a generator object
counter = count_up_to(10)

# Iterate over the generator object
for i in counter:
    print(i)

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

# Generators can also be used with the 'next' function
# to get the next value from the generator object

counter = count_up_to(5)

print(next(counter))
# Output: 5
print(next(counter))
# Output: 4
print(next(counter))
# Output: 3
print(next(counter))
# Output: 2
print(next(counter))
# Output: 1
print(next(counter))
# Output: 0

# The generator function can also take arguments
# and the 'send' method can be used to pass values into the generator

def counter_generator(start, end):
    # The generator function is defined with arguments
    # The 'yield' keyword is used to yield a value
    # and the 'send' method is used to pass a value into the generator
    current = start
    while current < end:
        value = yield current
        if value is not None:
            current = value
        else:
            current += 1

# Create a generator object
counter = counter_generator(5, 10)

# Iterate over the generator object
for i in range(5, 10):
    print(next(counter))

# Output:
# 5
# 6
# 7
# 8
# 9

# The 'send' method can be used to pass a value into the generator
counter = counter_generator(5, 10)

# Send a value into the generator
counter.send(7)
# Output: 7

# The generator continues from where it left off
counter.send(8)
# Output: 8
counter.send(9)
# Output: 9