i = 0;
room = ["1/1","1/2","1/3"]

#while loop
while i < 5 :                       #while statement is true do it
    print(i ,end = " ");
    i = i + 1;
print(" ");
print("while loop");

#for loop
for i in room :                     #do i in room number
    print(i ,end = " ");
print(" ");
print("for loop");

#range
for i in range(5) :                 #range(5) is 0,1,2,3,4
    print(i ,end = " ");
print(" ");
for i in range(1,5) :               #range(1,5) is 1,2,3,4,
    print(i ,end = " ");
print(" ");
for i in range(2,10,2) :            #range(2,10,2) is 2,4,6,8
    print(i ,end = " ");
print(" ")

#break
for i in range(10) :                #stop loop if i == 5
    if i == 5 :
        break;
    print(i ,end = " ");
print(" ")

#continue
for i in range(1,11) :              #if i == 5 continue the loop
    if i == 5 :
        continue;
    print(i ,end = " ");
print(" ")

#else with loop
names = ["Mateo", "John" , "Eric:" , "Mark" , "Rober"];

search = "John";
for n in names:                     #do n in name
    if search == n :                #if searh == n print()
        print(search + ' is found in list');
        break;
else :
    print('Not found!');            #if not true do this