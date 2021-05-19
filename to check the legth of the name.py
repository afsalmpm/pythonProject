print(' ')
name= input("enter your full name ")
name_length=len(name)
while name_length <5 or name_length>50:
    if name_length<5:
        print('minmum 5 charactors required')
    elif name_length >50:
        print("maximum of 50 charectors only")
    name = input("enter your full name ")
    name_length = len(name)
print(' ')
print('Thank you for typing your name correctly ')
print(f"your name is {name}")
