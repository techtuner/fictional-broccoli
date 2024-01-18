import os

message = """

This is a script to create folders and files in a sequence with a particular filename followed by the sequence number

Eg: 'day 01/day01.<file-extension>' 'day 02/day02.<file-extension>' 'day 03/day03.<file-extension>'...... 'day n/dayn.<file-extension>'

"""

current_path = os.getcwd()
file_name = input("What should be the fileName: ")
start_range= int(input("What is the beginning number: "))
end_range= int(input("What is the endding number: "))
file_extension = input("What type of file do you want it to be: ")
for i in range(start_range, end_range + 1):
    os.mkdir(f"{file_name}{i}")
    os.chdir(f"{file_name}{i}")
    os.system(f"type nul > {file_name}{i}.{file_extension}")
    os.chdir(current_path)