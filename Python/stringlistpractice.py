first_string = "If monkeys like bananas, then I must be a monkey!"
print first_string.find("monkey")
print first_string.replace("monkey","alligator")

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x2 = ["hello",2,54,-2,7,12,98,"world"]
print x2[0]
print x2[len(x2)-1]
x3 = []
x3.append(x2[0])
x3.append(x2[len(x2)-1])
print x3

x4 = [19,2,54,-2,7,12,98,32,10,-3,6]
x4.sort()
x5 = x4[:5]
x4= x4[5:]
x4.insert(0,x5)
print x4
