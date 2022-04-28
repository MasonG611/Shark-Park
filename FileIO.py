file = open('States.txt', 'r+')
print ("Name of File: ", file.name)
print (file.readlines())
file.close()


file = open('States.txt', 'r+')

file.seek(0, 2)
print(file.readline())
eof = file.tell()
print(eof)
file.seek(0, 0)
nextLine = True
while nextLine:
    print(file.readline())
    print(file.tell())
    if file.tell() == (eof-7) or file.tell() == (eof-5):
        print(eof)
        print(file.tell())
        lastline = file.readline()
        nextLine = False
        print('line is ', lastline)

file.write('Open\n')
file.close()
