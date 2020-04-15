def hello() :               #baic function
    print("hello");

def pr(message) :           #basic function
    print(message);

def qM(x, y) :              #return function
    return x + y;

def create_button(id, color = '#ffffff', text = 'Button', size = 16):  #Keyword Arguments
    print('Button ID: %d' % id);
    print('Attributes:');
    print('Color: %s' % color);
    print('Text: %s' % text);
    print('Size: %d px' % size);
    print();

z = lambda x,y : x+y;       #lambda function
print(z(3,5));
