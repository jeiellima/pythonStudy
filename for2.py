#Finding the largest number

largest_number = -1

for numb in [9,41,12,3,74,15]:
    if numb > largest_number:
        largest_number = numb
    print(largest_number, numb)

#Finding the smallest number
"""
smallest_number = 100

for number in [9,41,12,3,74,15,-1]:
    if number < smallest_number:
        smallest_number = number
    print(smallest_number, number)

    #INCORRECT
""" 

smallest = None
for value in [9,41,12,3,74,15,-1]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After:", smallest)




