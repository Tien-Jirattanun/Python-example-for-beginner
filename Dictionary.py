#*Dictionary can call the data in Dictionary by useing keyword
#Way to use dictionary

scores = {"M" : 100, "L" : 80, "A" : 70, "T" : 60};
scores['bobby'] = 10;                                                 #append bobby

number = {1 : "one", 2 : "Two"};

print(scores);
print(number);
print("=============================================");
#How to use dictionary

#display
print("T =>", scores["T"])
print("L =>",scores["L"]);

#update data
scores["T"] = scores["T"] + 100;
scores["M"] = 200

print(scores["T"]);
print(scores["M"]);
print("==============================================");

#check dictionary
if "K" in scores.keys() :
    print(scores["smith"]);
else :
    print("no smith in scores");

#loop with dictionary
alphabets = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}

for k, v in alphabets.items():
    print(k, v)

# iterate through keys
print('Key :', end = " ");
for k in alphabets.keys():
    print(k, end = " ");

print();

# iterate through values
print('Value :', end = " ");
for v in alphabets.values():
    print(v, end = " ");