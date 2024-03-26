def filter_even_numbers(num):
    #returns only even numbers
    return num % 2 == 0
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,35,57,58]

for num in filter(filter_even_numbers,nums):
    print(num)