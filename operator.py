x = 25;
y = 5;
io = 1;

#Arithmetic operator(math)

print(x+y);                              #x + y
print(x-y);                              #x - y
print(x*y);                              #x(y)
print(x/y);                              #x divided
print(x//y);                             #floor number to integer
print(x%y);                              #get division remainder
print(x**y);                             #power

#Comparison operator(true or false)

print(x<y);                              #x < y
print(x<=y);                             #x < or = y
print(x>y);                              #x > y
print(x>=y);                             #x > or = y
print(x==y);                             #x = y
print(x!=y);                             #x not = y

#Logical operators(use in if else)

if x == 25 and y == 5 :
    print("and is x == 25 and y == 25 true of false");
elif x == 25 or y == 5 :
    print("or x == 25 of y = 5 true of false");

#Sequence Operators(True false)

room = ["1/1","1/2","1/3"];

print("1/1" in room);
print("1/2" not in room);
