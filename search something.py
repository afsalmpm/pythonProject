x=input('what do you want to search ')
found=False
for y in str([1,4,3,6,7,7,6]):
    if y==x:
        found=True
        print(f'found {x}')
        break
    #print(y) #To check if the break is working
if found==False:
    print(f'{x} is not foud')
