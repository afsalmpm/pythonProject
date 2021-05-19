import csv


class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is in IIS")


Boys_list = [["Name", "Age"]]


class Boys(Students):
    def add_to_list(self):
        Boys_list.append([self.name, self.age])

    def talk(self):
        print(f"{self.name} barks")


Girls_list = [["Name", "Age"]]


class Girls(Students):
    def add_to_list(self):
        Girls_list.append([self.name, self.age])

    def talk(self):
        print(f"{self.name} Meows")


loop = " "
while loop != "x":
    which_mam = input('Press "b" for boys and "g" for girls ')

    if which_mam == "g":
        x = input("The girl's name ")
        y = input("The girl's age ")
        x = Girls(x, y)
        x.add_to_list()
    elif which_mam == "b":
        x = input("The boy's name ")
        y = input("The boy's age ")
        x = Boys(x, y)
        x.add_to_list()
    else:
        print("unknown")
    loop = input('Press "x" to exit .. press enter to redo ')


# data to be written row-wise in csv fil
data = Girls_list

# opening the csv file in 'w+' mode
file = open('Girls.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)

# data to be written row-wise in csv fil
data = Boys_list

# opening the csv file in 'w+' mode
file = open('Boys.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)
