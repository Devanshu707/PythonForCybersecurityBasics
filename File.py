# # The keyword with handles errors and manages external resources when used with other functions. In this case, it's used with the open() function in order to open a file. It will then manage the resources by closing the file after exiting the with statement.
# with open("file1.txt", "r") as file:
#     file_text = file.read()
# print(file_text)

# line = "jrafael,192.168.243.140,4:56:27,True"
# with open("file1.txt", "a") as file:
#     file.write(line)
# open("file1.txt")

# parsing: the process of converting data into a more readable format
#split() converts a string into a list
# string1 = """Hello, How are you.
# I am good today.
# How are you"""
# list1 = string1.split()
# print(list1)

# approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
# print("before .split():", approved_users)
# approved_users = approved_users.split(",")
# print("after .split():", approved_users)

# The .join() method concatenates the elements of an iterable into a string. The syntax used with .join() is distinct from the syntax used with .split() and other methods that you've worked with, such as .index().
# approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# print("before .join():", approved_users)
# approved_users = ",".join(approved_users)
# print("after .join():", approved_users)
