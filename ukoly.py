f = open("test1.txt", "w")
f.write("Hello world file")
f.close()

def print_hi(name):

    print(f'Hi, {name}')  

f2 = open("test1.txt", "r")
data = f2.read()
f2.close()

if __name__ == '__main__':
    print_hi('PyCharm')

print(data)