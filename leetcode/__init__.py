a = ['1','2','3','4','5']
b=""
for i in a[0:len(a)-1]:
    b += i+","

b = b+a[-1]
print(type(b))