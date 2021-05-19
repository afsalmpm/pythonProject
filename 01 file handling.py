file_path = "C:\\Users\\dell\\Desktop\\"
file_name = "test for file handling"


try:
    with open(f"{file_path}{file_name}.txt", "x") as file:  # 'x' as keyword argument to create a new file
        file.write(f"{file_path}\n")
except FileExistsError:
    with open(f"{file_path}{file_name}.txt", "a") as file:  # 'r+' as keyword to open/read/write an existing file
        file.write(f"{file_path}\n")

with open(f"{file_path}{file_name}.txt", "r") as file:
    x = file.read()
print(x)


'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''








# try:
#     f = open("01_myfile.txt", "x")  # to create a new file

# except FileExistsError:
#     f = open("01_myfile.txt", "r+")  # To open an existing file
#     for x in range(123):
#         f.write("what is this \n")  # f.write is for reading
# x = f.readline()
#
# print(x)
# f.close()




