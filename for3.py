#Continuing in a loop
""""
zork = 0
print("Before:", zork)
for thing in [9,41,12,3,74,15]:
    zork += 1
    print(zork, thing)
print("After:", zork) 

"""
#Summing in a loop

zork = 0
print("Before:", zork)
for thing in [9,41,12,3,74,15]:
    zork += thing
    print(zork, thing)
print("After:", zork)

#Finding the Average in a Loop

count = 0
sum = 0
print("Before:", count, sum)

for value in [9,41,12,3,74,15]:
    count += 1
    sum += value
    print(count, sum, value)
print("After:", count, sum, sum/count)

#Filtering in a loop

for number in [9,41,12,3,74,15]:
    if number > 20:
        print("Large number:", number)

#Searching using a boolean

found = False

for value1 in [9,41,12,3,74,15]:
    if value1 == 3:
        found = True
        break
    print(found, value1)