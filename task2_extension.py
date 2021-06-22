####using python os module splitext() function####
import os
split_tup=os.path.splitext('task1.py')
print(split_tup)
file_name=split_tup[0]
file_extension=split_tup[1]
print("File Name: ",file_name)
print("File Extension: ",file_extension)

####using Pathlib module####
import pathlib
file_extension=pathlib.Path('task1.py').suffix
print("file extension: ",file_extension)

