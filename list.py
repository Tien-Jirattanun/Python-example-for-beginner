numbers = [-1, 2, 5, 8, 10, 13];                                 #list int
names = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke'];           #list string
mixed_type = [-2, 5, 84.2, "Mountain", "Python"];                #list mix

#apendlist

numbers.append(7);

#set data in list

print('names[0] = ', names[0]);                 #Metro
print('names[-1] = ', names[-1]);               #Luke
names[0] = "Tien";
print('names[0] = ',names[0]);                  #Tien
del(names[0]);
print("====================================================");

#for with list

for i in names :
    print(i, end = " ");

print("====================================================");

#List slicing

ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

a = ch[0:4]                     # a - d
b = ch[4:9]                     # e - h
c = ch[:3]                      # a - c
d = ch[3:]                      # c - h
e = ch[:]                       # copy all list, or equivalent to e = ch
f = ch[0:2] + ch[6:8]           # a - b and g - h

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

