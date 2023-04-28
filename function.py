#Function Example1
def printHello():
    print('hello')
printHello()

print("....")

#Function Example2
def printHello(val):
    print('hello',val)
printHello("python")

#Function Example3
def sum(val1,val2):
    return val1+val2
print("sum:", sum(10,4))


#Function Example4
list1=[2,4,7,8,9,7,6,5,5,4,4] 
list2=[45,66,77,88,55,7,7]
print('MAX number in array list1 is',max(list1) )
print ('MAX number in array list2 is',max(list2))
def max(list):
    maxnumber = list[0]
    for x in list:
        if maxnumber < x:
            maxnumber= x
    return maxnumber

# Function definition is here
def changeme( mylist ):

   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: "), mylist
   return

    # Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


# Function definition is here
def changeme( mylist ):
    mylist.append([1,2,3,4])
    print ("Values inside the function: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)