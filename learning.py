firstval = 30
secondval = firstval
thirdval = 30.00
print(firstval is secondval)
print(thirdval is secondval)
if thirdval is secondval == "True":
    print("It is of the same entity")
else:
    print("it is not of the same entity")
a = ["john","Joseph","George", "Abel"]
print(a[0])
print(a[3])
a[2] = "Paul"
print(a)
for times in a:
    print(times)
rep = 0
while rep<len(a):
    print(a[rep])
    rep = rep + 1
print("All done")
firstRange = range(11)
secondRange = range(20) 
thirdRange = range(21,30)
discount1 = 0
discount2 = 0.10
discount3 = 0.15
itemsOrdered = int(input("enter the number of items ordered : "))
if itemsOrdered in firstRange:
    customerdiscount = discount1
    print("the customer's discount is " + str(customerdiscount))
else:
    if itemsOrdered in secondRange:
        customerdiscount = discount2
        print("the customer's discount is " + str(customerdiscount))
    else:
        if itemsOrdered <= thirdRange:
            customerdiscount = discount3
            print("the customer's discount is " + str(customerdiscount))
        else:
            print("Item number doesnt have a customer discount")
print("All done baby")
# this will only work for integers                        
arr = [[[4,3,0,[0,1]],[7,8]],[4,5,7],[2,7,8],[4,8,7,]]
#for counter in arr:
#    print(counter)
cout = 0
while cout<len(arr):
    print(arr[cout])
    cout = cout + 1
    
         

    
