number = 0
total = 0.0

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    number += 1
    total += fval

print("All done!")
print(total,"/",number,"=",total/number)