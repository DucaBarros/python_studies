import pathlib

# Creating files

myfile = pathlib.Path('test.py')

if myfile.exists() == False:
    print('Yes, I am here!')
else:
    print('Where am I?')