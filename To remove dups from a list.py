x=[1,3,5,6,3,4,9,4,73,3,3,1,3,4,5,6]
y=[]
for x in x:
    if x not in y:
        y.append(x)
print(y)