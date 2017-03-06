#odd even
def odd_even(num):
    for i in range (1, num):
        if i % 2 == 1:
            print "Number is", str(i) + ".", "This is an odd number." # str function changes i into string
        else:
            print "Number is", str(i) + ".", "This is an even number."

#multiply
def multiply(a,num):
    newlist = []
    for i in range(len(a)):
        newlist.append(a[i]*num)
    return newlist
