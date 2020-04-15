name = "jirattanun";                            #name is string we can use " " to tell compiler that in " " is string
nickname = 'Tien';                              #we can use ' ' to
intro = "I'm student";
intro2 = "My name is \"Tien\"";                 #if you want to put" or ' in string use \ before it
my_number = 'One '\
'Two '\
'Three '                                        #if you need to connet the string in another lin use\ to connect
table = """\
variable
1.     name               jirattanun
2.     nickname           Tien
3.     intro              I'm student
4.     intro2             My name is "Tien"
""";                                            #use """\ """ you can custom your string

print(table);
print(name);
print(nickname);
print(intro);
print(intro2);
print(my_number);
print(nickname[1]);                             #you can chose location in the string that you want to print.Start with [0]
print(len(nickname));                           #you can use len() to count the alphabet in string