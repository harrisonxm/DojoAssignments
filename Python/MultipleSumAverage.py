#Multiplies part 1 and 2
for i in range (1,1001): # part 1 for loop for 1-1000
    print i

for i in range (5,1000000,5): # paet 2 loop for 5-1000000 with i steps incrementing by 5
    print i

#Sum list
a = [1,2,5,10,255,3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print sum

#Average list
a = [1,2,5,10,255,3]
sum = 0
for i in range(len(a)): #i in range(len(a) == (var i = 0; i < 6; i++)
    sum += a[i]
avg = sum / len(a)
print avg
