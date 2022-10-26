import re



char1 = '!'
char2 = '????'
mystr = "mystring!!!123234sample!!!\n!!!\ntesti!!!"
result = re.findall("!!!([^!!!]*)!!!", mystr)

f = open("C:/Users/WQuan/Documents/Traineeprogramm/Python/Untitled-1.sql")
lines = "".join(f.readlines())
print(lines)
result = re.findall("&&&&([^&&&&]*)&&&&", lines)


for i in result:
    print(i)


