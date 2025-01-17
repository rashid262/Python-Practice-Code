# d1 = {'name':'Rashid', 'age' : 23, 'Phone': 7525884368}
# print(d1,type(d1))

#Dictionary is ordered collection
#Duplicate keys are not allowed  (latest value will be considered)
#Duplicate values are allowed
#Dictionary is mutable

marks = {"Science" : 75, "Maths": 60, "Computer" : 80}
print(marks)
marks["Science"] = 89
print(marks)

#accessing keys and values

for i in marks.keys():
    print(i,end=" ") #returns keys

print()

for j in marks.values():
    print(j,end=" ") #returns values

print()

for k in marks.items():
    print(k,end=" ") #return key value pairs in tuples ('Science', 89) ('Maths', 60) ('Computer', 80)





