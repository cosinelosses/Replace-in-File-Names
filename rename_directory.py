import os

replace_this = input('chars to replace: ')
replacement = input('replace with: ')
where = input('where [condition]: ')

#  condition = input('if contains: ')

path = os.getcwd()

filenames = os.listdir(path)

for filename in filenames:
    filecount = filecount + 1
    #  print(filename)
    os.rename(filename, filename.replace(replace_this, replacement))