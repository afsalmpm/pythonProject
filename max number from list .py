x=[100,102,4,6,3,8,0,9,4,12,3,4,51,7]
print('for loop method to find the lagest number')
y=None
for z in x:
    if y==None:
        y=z
    if y<z:
        y=z
print(f'{y} is the largest number using for loop')
print('*****************************************')
print('Another method below...Using while loop and index method')
length= len(x)
print(f'Lnghth is {length}')
z=0
while z<(length-1): #since length is 13 max index is 012...12
    if x[z]<x[z+1]:
        lar=x[z+1]
    z=z+1
print(f'{lar} using while and length method....somthing is wrong with this method')
print('*****************************************')
print('Another method below addressing first number in the ist')
z=x[0]
for y in x:
    if z<y:
        z=y
print(z)

print('Another method below')
print(max(x)) # Max function can not be used when there are int and strings in a list
print('some list operations below')
x[2]='AFSAL'
print(x)
x.append('hana')
print(x)
x.pop()
print(x)

