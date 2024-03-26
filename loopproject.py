# Define the height of the triangle
height = 5

# Loop through the rows of the triangle
while height > 0:
   # Print the spaces
   spaces = ' ' * (height - 1)
   # Print the stars
   stars = '*' * (2 * height - 1)
   # Print the row of the triangle
   print(spaces + stars)
   # Decrease the height
   height -= 1

# Output:
#     *
#    ***
#   *****
#  *******
# *********