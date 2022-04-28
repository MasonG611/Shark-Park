file = open('States.txt', 'r+')
print ("Name of File: ", file.name)
print (file.readlines())
file.close()


file = open('States.txt')

file.seek(0, 2)
print(file.readline())
eof = file.tell()
print(eof)
file.seek(0, 0)
nextLine = True
while nextLine:
    print(file.readline())
    print(file.tell())
    if file.tell() == (eof-4) or file.tell() == (eof-5) or file.tell() == (eof-1):
        print(eof)
        print(eof-1)
        lastline = file.readline()
        nextLine = False
        print('line is ', lastline)
file.close()
